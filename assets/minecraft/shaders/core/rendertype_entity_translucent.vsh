#version 150

#moj_import <light.glsl>
#moj_import <fog.glsl>

in vec3 Position;
in vec4 Color;
in vec2 UV0;
in ivec2 UV1;
in ivec2 UV2;
in vec3 Normal;

uniform sampler2D Sampler0;
uniform sampler2D Sampler1;
uniform sampler2D Sampler2;

uniform mat4 ModelViewMat;
uniform mat4 ProjMat;
uniform mat3 IViewRotMat;
uniform int FogShape;

uniform vec3 Light0_Direction;
uniform vec3 Light1_Direction;

out float vertexDistance;
out vec4 vertexColor;
out vec4 lightMapColor;
out vec4 overlayColor;
out vec2 texCoord0;
out vec4 normal;

flat out int stache;
flat out float isFace;

bool checkStache(ivec2 pixel) {
    vec4 color = texelFetch(Sampler0, pixel, 0);
    return ivec3(round(color.rgb * 255.0)) == ivec3(31, 32, 29);
}

vec3 getContrast(int layer) {
    vec3 t0 = vec3(1.0);
    vec3 t1 = vec3(0.0);

    for(int i = 8; i < 16; i++) { 
        vec3 col = texelFetch(Sampler0, ivec2(i, layer), 0).rgb;
        t0 = min(t0, col);
        t1 = max(t1, col);
    }

    return t1 - t0;
}

void main() {

    gl_Position = ProjMat * ModelViewMat * vec4(Position, 1.0);
    vertexDistance = fog_distance(ModelViewMat, IViewRotMat * Position, FogShape);
    vertexColor = minecraft_mix_light(Light0_Direction, Light1_Direction, Normal, Color);
    lightMapColor = texelFetch(Sampler2, UV2 / 16, 0);
    texCoord0 = UV0;
    normal = ProjMat * ModelViewMat * vec4(Normal, 0.0);
}

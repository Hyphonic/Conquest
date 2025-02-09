import os
import re

def get_model_name(filename):
    # Just remove the extension
    return os.path.splitext(filename)[0]

def process_yaml_template(model_name):
    template = '''{}:
  Type: armorstand
  Display: ''
  Health: 999
  Options:
    NoDamageTicks: 60
    PreventRandomEquipment: true
    Collidable: true
    MovementSpeed: 0
    NoGravity: true
    Invincible: true
    KnockbackResistance: 1
    Despawn: false
    AlwaysShowName: false
  Skills:
    - model{{m={};save=true}} @self ~onSpawn
    - model{{m={};save=true;delay=5}} @self ~onLoad
  Disguise: FALLING_BLOCK STONE
'''.format(model_name, model_name, model_name)
    return template

def main():
    models_path = r"C:\Users\hypho\Documents\BBModels"
    output_path = r"C:\Users\hypho\Documents\Conquest\scripts\MythicMobsExample.yml"
    
    # Get all files in the BBModels directory
    model_files = [f for f in os.listdir(models_path) if os.path.isfile(os.path.join(models_path, f))]
    
    # Generate YAML content for each model
    full_yaml = ""
    for model_file in model_files:
        model_name = get_model_name(model_file)
        full_yaml += process_yaml_template(model_name) + "\n"
    
    # Write to output file
    with open(output_path, 'w') as f:
        f.write(full_yaml.rstrip())
    
    print(f"Generated configurations for {len(model_files)} models in {output_path}")

if __name__ == "__main__":
    main()
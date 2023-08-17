import re

def increment_version(current_version, increment_type):
    feat, fix, patch = map(int, current_version.split('.'))
    
    if increment_type == 'feat':
        feat += 1
        fix = 0
        patch = 0
    elif increment_type == 'fix':
        fix += 1
        patch = 0
    elif increment_type == 'patch':
        patch += 1
    else:
        print("Invalid increment type")
        return current_version
    
    new_version = f"{feat}.{fix}.{patch}"
    return new_version

def main():
    current_version = input("Enter current version): ")
    if not current_version:
        current_version = '0.0.0'
    increment_type = input("Enter increment type (feat/fix/patch): ")
    
    if re.match(r'\d+\.\d+\.\d+', current_version) and increment_type in ['feat', 'fix', 'patch']:
        new_version = increment_version(current_version, increment_type)
        print(f"New version: {new_version}")
    else:
        print("Invalid input format.")

if __name__ == "__main__":
    main()

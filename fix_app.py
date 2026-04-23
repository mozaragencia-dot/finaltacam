import sys

with open('app.js', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if 171 <= i <= 4281:
        if line.startswith('  '):
            new_lines.append(line[2:])
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

# Add the closing brace for applyRoleAccess at line 171
new_lines.insert(171, '}\n')

with open('app.js', 'w') as f:
    f.writelines(new_lines)

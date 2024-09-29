import os, site

if __name__ == '__main__':
    path = input('Package path: ')
    site_package_dir = site.getsitepackages()[1]
    print(site_package_dir)

    output_dir = os.path.join(site_package_dir, os.path.basename(path))

    if os.path.exists(output_dir): exit('Package already installed.')
    else: os.makedirs(output_dir)

    for package_file in os.listdir(path):
        print(f'Cloning file {package_file}')
        with open(f'{path}\\{package_file}', 'r') as file:
            content = file.read()
            with open(f'{output_dir}\\{package_file}', 'w') as cloned_file:
                cloned_file.write(content)
        print('Cloned')
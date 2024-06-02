import os
import subprocess
import docker
from PyInquirer import prompt, Separator


def ask_questions():
    questions = [
        {
            'type': 'input',
            'name': 'project_name',
            'message': 'Project name:',
        },
        {
            'type': 'list',
            'name': 'cuda_image',
            'message': 'Select CUDA image:',
            'choices': [
                '11.3.1-cudnn8-devel-ubuntu20.04',
                '12.4.1-cudnn-devel-ubuntu22.04',
                Separator(),
                'Other',
            ],
        },
        {
            'type': 'input',
            'name': 'cuda_image_other',
            'message': 'Enter CUDA image:',
            'when': lambda answers: answers['cuda_image'] == 'Other',
        },
        {
            'type': 'list',
            'name': 'code_server_version',
            'message': 'Select Code Server version:',
            'choices': ['4.89.1', '3.10.2', '2.1698', Separator(), 'Other'],
        },
        {
            'type': 'input',
            'name': 'code_server_version_other',
            'message': 'Enter Code Server version:',
            'when': lambda answers: answers['code_server_version'] == 'Other',
        },
        {
            'type': 'input',
            'name': 'novnc_width',
            'message': 'noVNC display width (leave blank for default 1024):',
            'default': '1024',
        },
        {
            'type': 'input',
            'name': 'novnc_height',
            'message': 'noVNC display height (leave blank for default 768):',
            'default': '768',
        },
        {
            'type': 'input',
            'name': 'project_volume',
            'message': 'Project volume:',
        },
    ]

    answers = prompt(questions)

    # Handle optional inputs
    cuda_image = (
        answers['cuda_image_other'] if 'cuda_image_other' in answers else answers['cuda_image']
    )
    code_server_version = (
        answers['code_server_version_other']
        if 'code_server_version_other' in answers
        else answers['code_server_version']
    )
    novnc_width = answers['novnc_width'] if answers['novnc_width'] else '1024'
    novnc_height = answers['novnc_height'] if answers['novnc_height'] else '768'

    return {
        'project_name': answers['project_name'],
        'cuda_image': cuda_image,
        'code_server_version': code_server_version,
        'novnc_width': novnc_width,
        'novnc_height': novnc_height,
        'project_volume': answers['project_volume'],
    }


def deploy_container():
    answers = ask_questions()

    # Set environment variables
    os.environ['PROJECT_NAME'] = answers['project_name']
    os.environ['CUDA_IMAGE'] = answers['cuda_image']
    os.environ['CODE_SERVER_VERSION'] = answers['code_server_version']
    os.environ['PROJECTS_VOLUME'] = answers['project_volume']
    os.environ['NOVNC_WIDTH'] = answers['novnc_width']
    os.environ['NOVNC_HEIGHT'] = answers['novnc_height']
    os.environ['UID'] = str(os.getuid())
    os.environ['GID'] = str(os.getgid())

    compose_env = os.environ.copy()
    # Run docker-compose up with the environment variables
    subprocess.run(['docker', 'compose', 'up', '-d'], check=True, env=compose_env)

    # Initialize Docker client
    client = docker.from_env()

    # Get container information
    container_cs = client.containers.get(f'{answers["project_name"]}-gpu-cs-1')
    container_novnc = client.containers.get(f'{answers["project_name"]}-gpu-novnc-1')

    ip_cs = container_cs.attrs['NetworkSettings']['Networks']['gpu-network']['IPAddress']
    ip_novnc = container_novnc.attrs['NetworkSettings']['Networks']['gpu-network']['IPAddress']

    print(f"Container {answers['project_name']}-cs is running on IP {ip_cs} and port 8443")
    print(f"Container {answers['project_name']}-novnc is running on IP {ip_novnc} and port 6060")


if __name__ == '__main__':
    deploy_container()

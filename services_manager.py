import click
import os
import shutil
import subprocess
import sys


DQRCG_HOME = os.environ.get("DQRCG_HOME")

@click.group()
def cli():
 if not DQRCG_HOME:
        click.secho(f"Please set the DQRCG_HOME environment variable.", fg="red")
        sys.exit(2)

@cli.command()
def build():
    click.echo('Building the frontend')
    build_dir = os.path.join(DQRCG_HOME, "dqrcg", "client")
    status = subprocess.run(args=["npm", "run", "build"],cwd=build_dir, check=True)
    try:
        shutil.rmtree(os.path.join(DQRCG_HOME, "api", "build"))
    except: pass
    shutil.move(os.path.join(build_dir, "build"), os.path.join(DQRCG_HOME, "api"))
    click.secho("Building the frontend complete.", fg="green")

@cli.command()
def run_server():
    env_vars = {"FLASK_APP":"api/app.py",  "FLASK_ENV":"development", "VIRTUAL_ENV":"/Users/abhinayyadav/work/DQRCG/venv", "PATH":"/Users/abhinayyadav/work/DQRCG/venv/bin"}
    subprocess.run(args=["./run.sh"],cwd=DQRCG_HOME, env=env_vars, check=True, shell=True)



cli.add_command(build)
cli.add_command(run_server)


   
        

if __name__ == '__main__':
    cli()

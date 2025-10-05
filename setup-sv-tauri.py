import subprocess, os, sys, shutil, argparse

# Manual Info --------------------------------------------------------------------------------------

default_project_root = r"C:\Users\kotsu\Desktop\TestProject\Setup Script\Test"

# Parsing args ---------------------------------------------------------------------------
parser = argparse.ArgumentParser(description="Setup a SvelteKit + Tauri project.")

# Define arguments
parser.add_argument("path", help="absolute path to the project directory or '.' for current directory", nargs="?")
parser.add_argument("--clean", action="store_true", help="delete and remake the project directory")

# Parse arguments
args = parser.parse_args()

# Project Directory ------------------------------------------------------------------------------------------
if args.path:
    try:
        project_dir = os.path.abspath(args.path)
    except:
        print("Invalid path provided in args. Quitting.")
        sys.exit(1)
else:
    try:
        # Set path to defined manual path
        project_dir = os.path.abspath(default_project_root)
    except:
        print("Invalid default path. Quitting.")
        sys.exit(1)

# Default App name and Window name
project_window_name = os.path.basename(project_dir)
project_slug_name = project_window_name.lower().replace(" ", "-")

# Clean project dir if exists and --clean is specified -----------------------------------------------------
if args.clean:
    if os.path.exists(project_dir):
        shutil.rmtree(project_dir)

# Create Project Directory ----------------------------------------------------------------------------------

def run_command(cmd):
    subprocess.run(cmd, shell=True, capture_output=False, text=True)

os.makedirs(project_dir, exist_ok=True)
os.chdir(project_dir)

# Create minimal SvelteKit project
run_command("npx sv create . --template minimal --types ts --no-add-ons --no-install")

# Add features -----------------------------------------------------------------------------------------------
# Go to https://svelte.dev/docs/cli/sv-add to customize

addons = "npx sv add"

# Prettier
addons += " prettier"
# ESLint
addons += " eslint"
# Tailwind CSS with typography and forms plugins
addons += " tailwindcss=\"plugins:typography,forms\""
# Vitest with unit test usages
addons += " vitest=\"usages:unit\""
# SvelteKit adapter static
addons += " sveltekit-adapter=\"adapter:static\""
# mdsvex
addons += " mdsvex"
# Storybook
# addons += " storybook"

# Install addons
run_command(addons + " --no-install")

# Install tauri cli and JS API
print("[Adding Tauri packages...]")
run_command("npm add --save-dev @tauri-apps/cli@latest --silent --no-install")
run_command("npm add @tauri-apps/api@latest --silent --no-install")

# Install dependencies
print("[Running install, stand by...]")
run_command("npm install")

# Tauri Init
run_command(
    f'npx tauri init --ci -A {project_slug_name} -W {project_window_name} -D "../build" -P "http://localhost:5173" --before-dev-command "npm run dev" --before-build-command "npm run build"',
)

# Add layout.ts file with prerendering = true, ssr = false
with open(os.path.join(project_dir, "src", "routes", "layout.ts"), "w") as f:
    f.write("""export const prerender = true; \nexport const ssr = false;""")

print("\n\n[=======================================================================================]")
print(f"| Tauri + Sveltekit setup complete in: \n| {project_dir}")
print("| =======================================================================================")
print("| Before running, set the unique identifier in src-tauri/tauri.conf.json and")
print("| change the app and windows names from the default (the project folder name).\n")
print("| Run 'npx tauri dev' from root or 'cargo tauri dev' from the src-tauri directory.")
print("[=======================================================================================]")
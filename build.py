import os
import shutil
import re

def minify_css(content):
    # Remove comments
    content = re.sub(r'/\*[\s\S]*?\*/', '', content)
    # Remove whitespace
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'\s*([{:;,])\s*', r'\1', content)
    content = content.replace(';}', '}')
    return content.strip()

def minify_js(content):
    # Remove single line comments
    content = re.sub(r'//.*', '', content)
    # Remove multi-line comments
    content = re.sub(r'/\*[\s\S]*?\*/', '', content)
    # Remove whitespace (very basic)
    content = re.sub(r'\s+', ' ', content)
    # content = re.sub(r'\s*([=+\-*/{}:;,()])\s*', r'\1', content)
    return content.strip()

def minify_html(content):
    # Remove comments
    content = re.sub(r'<!--(?!\[if).*?-->', '', content, flags=re.DOTALL)
    # Remove whitespace between tags
    content = re.sub(r'>\s+<', '><', content)
    return content.strip()

def build():
    # Setup directories
    base_dir = os.getcwd()
    build_dir = os.path.join(base_dir, 'build')
    
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)
    os.makedirs(os.path.join(build_dir, 'css'))
    os.makedirs(os.path.join(build_dir, 'js'))
    os.makedirs(os.path.join(build_dir, 'assets'))

    # Process CSS
    print("Processing CSS...")
    css_files = ['variables.css', 'base.css', 'layout.css', 'components.css', 'animations.css']
    combined_css = ""
    for css_file in css_files:
        with open(os.path.join(base_dir, 'css', css_file), 'r') as f:
            combined_css += f.read() + "\n"
    
    minified_css = minify_css(combined_css)
    with open(os.path.join(build_dir, 'css', 'style.min.css'), 'w') as f:
        f.write(minified_css)

    # Process JS
    print("Processing JS...")
    with open(os.path.join(base_dir, 'js', 'main.js'), 'r') as f:
        js_content = f.read()
    
    minified_js = minify_js(js_content)
    with open(os.path.join(build_dir, 'js', 'main.min.js'), 'w') as f:
        f.write(minified_js)

    # Process HTML
    print("Processing HTML...")
    with open(os.path.join(base_dir, 'index.html'), 'r') as f:
        html_content = f.read()
    
    # Replace CSS links
    # Remove existing CSS links and imports
    html_content = re.sub(r'<link rel="stylesheet" href="css/style.css">', '<link rel="stylesheet" href="css/style.min.css">', html_content)
    
    # Replace JS script
    html_content = re.sub(r'<script src="js/main.js"></script>', '<script src="js/main.min.js"></script>', html_content)
    
    minified_html = minify_html(html_content)
    with open(os.path.join(build_dir, 'index.html'), 'w') as f:
        f.write(minified_html)

    # Copy Assets
    print("Copying Assets...")
    if os.path.exists(os.path.join(base_dir, 'assets')):
        for item in os.listdir(os.path.join(base_dir, 'assets')):
            s = os.path.join(base_dir, 'assets', item)
            d = os.path.join(build_dir, 'assets', item)
            if os.path.isfile(s):
                shutil.copy2(s, d)

    # Copy Root Files (robots.txt, sitemap.xml)
    print("Copying Root Files...")
    root_files = ['robots.txt', 'sitemap.xml']
    for file in root_files:
        s = os.path.join(base_dir, file)
        d = os.path.join(build_dir, file)
        if os.path.exists(s):
            shutil.copy2(s, d)

    print("Build complete!")

if __name__ == "__main__":
    build()

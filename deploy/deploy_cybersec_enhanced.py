#!/usr/bin/env python3
"""
🌃 Cyberpunk AI Deployer - Cybersecurity Enhanced Edition v3.0
Automated deployment script for Open WebUI + Ollama with expanded cybersecurity models
"""

import os
import sys
import subprocess
import time
from datetime import datetime
import shutil
import json

# ANSI color codes for cyberpunk aesthetic
NEON_CYAN = '\033[96m'
NEON_PURPLE = '\033[95m'
NEON_GREEN = '\033[92m'
NEON_YELLOW = '\033[93m'
NEON_RED = '\033[91m'
NEON_BLUE = '\033[94m'
BRIGHT = '\033[1m'
DIM = '\033[2m'
RESET = '\033[0m'
BLINK = '\033[5m'

# Box drawing characters
BOX_TL = '╔'
BOX_TR = '╗'
BOX_BL = '╚'
BOX_BR = '╝'
BOX_H = '═'
BOX_V = '║'

# Expanded AI Models with Cybersecurity Focus
AI_MODELS = {
    "1": {
        "name": "Lily-Cybersecurity-7B",
        "model_id": "hf.co/segolilylabs/Lily-Cybersecurity-7B-v0.2-GGUF",
        "file": "lily-cybersecurity-7b-v0.2.Q5_K_M.gguf:latest",
        "size": "4.37 GB",
        "description": "🛡️ Specialized for cybersecurity analysis and pentesting",
        "use_cases": [
            "Vulnerability assessment",
            "Security code review",
            "Threat analysis",
            "Pentesting guidance",
            "Security best practices"
        ],
        "type": "Security",
        "ram_required": "8 GB"
    },
    "2": {
        "name": "Seneca-Cybersecurity-Q4",
        "model_id": "hf.co/AlicanKiraz0/Seneca-Cybersecurity-LLM-Q4_K_M-GGUF",
        "file": "Q4_K_M",
        "size": "~4.5 GB",
        "description": "🔐 Advanced cybersecurity analysis with Q4 quantization",
        "use_cases": [
            "Malware analysis",
            "Incident response",
            "Network security",
            "Security compliance",
            "Threat hunting"
        ],
        "type": "Security",
        "ram_required": "8 GB"
    },
    "3": {
        "name": "WhiteRabbitNeo-7B",
        "model_id": "hf.co/WhiteRabbitNeo/WhiteRabbitNeo-7B-v1.5a",
        "file": "WhiteRabbitNeo-7B-v1.5a",
        "size": "~4.5 GB",
        "description": "🐰 Offensive security and red team operations",
        "use_cases": [
            "Penetration testing",
            "Exploit development",
            "Red team tactics",
            "Security research",
            "CTF challenges"
        ],
        "type": "Security",
        "ram_required": "8 GB"
    },
    "4": {
        "name": "CyberGuard-7B",
        "model_id": "hf.co/omasteam/cyberguard-ai-security-analyzer",
        "file": "cyberguard-ai-security-analyzer",
        "size": "~4.8 GB",
        "description": "🛡️ Defensive security and blue team operations",
        "use_cases": [
            "SIEM analysis",
            "Log analysis",
            "Security monitoring",
            "Incident detection",
            "Blue team tactics"
        ],
        "type": "Security",
        "ram_required": "8 GB"
    },
    "5": {
        "name": "SecGPT-14B",
        "model_id": "hf.co/mradermacher/SecGPT-14B-GGUF",
        "file": "SecGPT-14B.Q4_K_M.gguf",
        "size": "~9.1 GB",
        "description": "🔒 Large security-focused model for complex analysis (Q4_K_M recommended, Q8_0 available for best quality)",
        "use_cases": [
            "Advanced threat analysis",
            "Security architecture",
            "Compliance auditing",
            "Risk assessment",
            "Security documentation"
        ],
        "type": "Security",
        "ram_required": "16 GB"
    },
    "6": {
        "name": "SecGPT-7B",
        "model_id": "hf.co/mradermacher/SecGPT-7B-i1-GGUF",
        "file": "SecGPT-7B.i1-Q4_K_M.gguf",
        "size": "~4.8 GB",
        "description": "🔒 Efficient security model with i1-Q4_K_M quantization (fast, recommended)",
        "use_cases": [
            "Security code analysis",
            "Threat assessment",
            "Vulnerability scanning",
            "Security best practices",
            "Compliance checking"
        ],
        "type": "Security",
        "ram_required": "8 GB"
    },
    "7": {
        "name": "Qwen2.5-Coder-7B",
        "model_id": "qwen2.5-coder:7b",
        "file": "qwen2.5-coder:7b",
        "size": "~4.7 GB",
        "description": "⚡ Advanced coding with security awareness",
        "use_cases": [
            "Secure code development",
            "Code review & refactoring",
            "Security patch development",
            "API security",
            "DevSecOps"
        ],
        "type": "Coding",
        "ram_required": "8 GB"
    },
    "8": {
        "name": "DeepSeek-R1",
        "model_id": "deepseek-r1:8b",
        "file": "deepseek-r1:distill-qwen-7b",
        "size": "~8 GB",
        "description": "🧠 Complex reasoning for security scenarios",
        "use_cases": [
            "Threat modeling",
            "Attack chain analysis",
            "Security strategy",
            "Risk calculation",
            "Incident reconstruction"
        ],
        "type": "Reasoning",
        "ram_required": "12 GB"
    },
    "9": {
        "name": "CodeShield-7B",
        "model_id": "hf.co/CodeShield/ThemisRM-Qwen2.5-7B-PMP",
        "file": "ThemisRM-Qwen2.5-7B-PMP",
        "size": "~4.5 GB",
        "description": "🛡️ Static code analysis and vulnerability detection",
        "use_cases": [
            "SAST analysis",
            "Code vulnerability scanning",
            "Security linting",
            "Dependency checking",
            "Code security review"
        ],
        "type": "Security",
        "ram_required": "8 GB"
    },
    "10": {
        "name": "Mixtral-8x7B-Instruct",
        "model_id": "mixtral:8x7b-instruct",
        "file": "mixtral:8x7b-instruct-v0.1-q4_K_M",
        "size": "~26 GB",
        "description": "🌟 Multi-expert model for comprehensive security analysis",
        "use_cases": [
            "Multi-domain security analysis",
            "Complex incident response",
            "Security architecture design",
            "Comprehensive auditing",
            "Expert-level consultation"
        ],
        "type": "General",
        "ram_required": "32 GB"
    }
}

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    """Display cyberpunk-themed banner"""
    banner = f"""
{NEON_CYAN}{BRIGHT}
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║   ███╗   ██╗███████╗ ██████╗ ███╗   ██╗                 ║
    ║   ████╗  ██║██╔════╝██╔═══██╗████╗  ██║                 ║
    ║   ██╔██╗ ██║█████╗  ██║   ██║██╔██╗ ██║                 ║
    ║   ██║╚██╗██║██╔══╝  ██║   ██║██║╚██╗██║                 ║
    ║   ██║ ╚████║███████╗╚██████╔╝██║ ╚████║                 ║
    ║   ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝                 ║
    ║                                                           ║
    ║      🔐 CYBERSECURITY ENHANCED EDITION v3.0 🔐           ║
    ║            サイバーセキュリティ強化版                       ║
    ║                                                           ║
    ║            10 Specialized Security Models                 ║
    ║                 Private • Powerful • Secure               ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
{RESET}
    """
    print(banner)

def print_box(title, content, color=NEON_GREEN):
    """Print content in a styled box"""
    lines = content.strip().split('\n')
    max_len = max(len(title), max(len(line) for line in lines)) + 4
    
    print(f"\n{color}{BOX_TL}{BOX_H * max_len}{BOX_TR}")
    print(f"{BOX_V} {BRIGHT}{title.center(max_len - 2)}{RESET}{color} {BOX_V}")
    print(f"{BOX_V}{BOX_H * max_len}{BOX_V}")
    
    for line in lines:
        print(f"{BOX_V} {line.ljust(max_len - 2)} {BOX_V}")
    
    print(f"{BOX_BL}{BOX_H * max_len}{BOX_BR}{RESET}")

def run_command(cmd, description="", capture_output=False):
    """Execute shell command with optional output capture"""
    if description:
        print(f"\n{NEON_BLUE}[*] {description}...{RESET}")
    
    try:
        if capture_output:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            return result.returncode == 0, result.stdout
        else:
            result = subprocess.run(cmd, shell=True)
            return result.returncode == 0, ""
    except Exception as e:
        print(f"{NEON_RED}[!] Error: {e}{RESET}")
        return False, ""

def check_docker():
    """Check if Docker is installed and running"""
    success, _ = run_command("docker --version", capture_output=True)
    if not success:
        return False
    
    success, _ = run_command("systemctl is-active docker", capture_output=True)
    return success

def install_docker():
    """Install Docker and Docker Compose"""
    print_box("Docker Installation", "Installing Docker Engine and Docker Compose", NEON_CYAN)
    
    commands = [
        ("apt-get update", "Updating package lists"),
        ("apt-get install -y ca-certificates curl gnupg", "Installing prerequisites"),
        ("install -m 0755 -d /etc/apt/keyrings", "Creating keyrings directory"),
        ("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg", "Adding Docker GPG key"),
        ('echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null', "Adding Docker repository"),
        ("apt-get update", "Updating package lists"),
        ("apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin", "Installing Docker components"),
        ("systemctl enable docker", "Enabling Docker service"),
        ("systemctl start docker", "Starting Docker service")
    ]
    
    for cmd, desc in commands:
        success, _ = run_command(cmd, desc)
        if not success:
            print(f"{NEON_RED}[!] Failed to install Docker{RESET}")
            return False
    
    print(f"{NEON_GREEN}[✓] Docker installed successfully!{RESET}")
    return True

def create_docker_compose(selected_model):
    """Create docker-compose.yml file"""
    compose_content = f"""version: '3.8'

services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    volumes:
      - ollama:/root/.ollama
    ports:
      - "11434:11434"
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: {AI_MODELS[selected_model]['ram_required']}
    networks:
      - ai-network

  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    volumes:
      - ./open_webui_data:/app/backend/data
    ports:
      - "3000:8080"
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434
      - WEBUI_SECRET_KEY=${{WEBUI_SECRET_KEY:-$(openssl rand -hex 32)}}
      - ENABLE_SIGNUP=true
    restart: unless-stopped
    depends_on:
      - ollama
    networks:
      - ai-network

volumes:
  ollama:
    driver: local

networks:
  ai-network:
    driver: bridge
"""
    return compose_content

def deploy_ai_system():
    """Main deployment function"""
    clear_screen()
    print_banner()
    
    print_box("🚀 AI System Deployment", "Starting deployment process...", NEON_CYAN)
    
    # Check Docker
    if not check_docker():
        print(f"{NEON_YELLOW}[!] Docker not found. Installing...{RESET}")
        if not install_docker():
            print(f"{NEON_RED}[!] Docker installation failed{RESET}")
            return False
    else:
        print(f"{NEON_GREEN}[✓] Docker is installed and running{RESET}")
    
    # Select AI model
    selected_model = select_ai_model()
    if not selected_model:
        return False
    
    # Create project directory
    project_dir = os.path.expanduser("~/open-webui")
    os.makedirs(project_dir, exist_ok=True)
    os.chdir(project_dir)
    
    print(f"\n{NEON_BLUE}[*] Creating project in: {project_dir}{RESET}")
    
    # Create docker-compose.yml
    compose_content = create_docker_compose(selected_model)
    with open("docker-compose.yml", "w") as f:
        f.write(compose_content)
    
    print(f"{NEON_GREEN}[✓] Docker Compose file created{RESET}")
    
    # Start services
    print(f"\n{NEON_CYAN}[*] Starting Docker containers...{RESET}")
    success, _ = run_command("docker compose up -d", "Starting services")
    
    if not success:
        print(f"{NEON_RED}[!] Failed to start services{RESET}")
        return False
    
    # Wait for services to be ready
    print(f"\n{NEON_YELLOW}[*] Waiting for services to initialize (30 seconds)...{RESET}")
    time.sleep(30)
    
    # Pull the selected model
    model_info = AI_MODELS[selected_model]
    print(f"\n{NEON_PURPLE}[*] Downloading {model_info['name']} model...{RESET}")
    print(f"{DIM}This may take 5-15 minutes depending on your connection speed{RESET}")
    
    # Construct the pull command based on model type
    if model_info['model_id'].startswith('hf.co/'):
        pull_cmd = f"docker exec -it ollama ollama pull {model_info['model_id']}"
    else:
        pull_cmd = f"docker exec -it ollama ollama pull {model_info['file']}"
    
    success, _ = run_command(pull_cmd, f"Pulling {model_info['name']}")
    
    if not success:
        print(f"{NEON_RED}[!] Failed to download model{RESET}")
        print(f"{NEON_YELLOW}[*] You can try downloading it manually later{RESET}")
    else:
        print(f"{NEON_GREEN}[✓] Model downloaded successfully!{RESET}")
    
    # Get server IP
    success, ip_output = run_command("curl -s ifconfig.me", capture_output=True)
    server_ip = ip_output.strip() if success else "YOUR_SERVER_IP"
    
    # Display success message
    print_box("✨ Deployment Complete!", f"""
Your AI system is now running!

Access Open WebUI: http://{server_ip}:3000
Model: {model_info['name']}
Type: {model_info['type']}

First user to sign up becomes admin.
Remember to disable signups after creating admin account!

Useful commands:
  cd ~/open-webui
  docker compose logs -f    # View logs
  docker compose restart     # Restart services
  docker compose down        # Stop services
  docker compose up -d       # Start services
""", NEON_GREEN)
    
    return True

def select_ai_model():
    """Interactive model selection with categories"""
    clear_screen()
    print_banner()
    
    print_box("🤖 Select Your AI Model", "Choose from our cybersecurity-focused collection", NEON_PURPLE)
    
    # Group models by type
    security_models = []
    coding_models = []
    general_models = []
    
    for key, model in AI_MODELS.items():
        if model['type'] == 'Security':
            security_models.append((key, model))
        elif model['type'] == 'Coding':
            coding_models.append((key, model))
        else:
            general_models.append((key, model))
    
    # Display Security Models
    print(f"\n{NEON_RED}{BRIGHT}🔐 CYBERSECURITY MODELS:{RESET}")
    print(f"{DIM}Specialized for security analysis, pentesting, and threat detection{RESET}\n")
    
    for key, model in security_models:
        print(f"  {NEON_CYAN}[{key}]{RESET} {BRIGHT}{model['name']}{RESET}")
        print(f"      {DIM}Size: {model['size']} | RAM: {model['ram_required']}{RESET}")
        print(f"      {model['description']}")
        print()
    
    # Display Coding Models
    if coding_models:
        print(f"\n{NEON_BLUE}{BRIGHT}💻 CODING MODELS:{RESET}")
        print(f"{DIM}Optimized for secure code development and analysis{RESET}\n")
        
        for key, model in coding_models:
            print(f"  {NEON_CYAN}[{key}]{RESET} {BRIGHT}{model['name']}{RESET}")
            print(f"      {DIM}Size: {model['size']} | RAM: {model['ram_required']}{RESET}")
            print(f"      {model['description']}")
            print()
    
    # Display General Models
    if general_models:
        print(f"\n{NEON_GREEN}{BRIGHT}🌟 GENERAL/REASONING MODELS:{RESET}")
        print(f"{DIM}Advanced reasoning and multi-domain capabilities{RESET}\n")
        
        for key, model in general_models:
            print(f"  {NEON_CYAN}[{key}]{RESET} {BRIGHT}{model['name']}{RESET}")
            print(f"      {DIM}Size: {model['size']} | RAM: {model['ram_required']}{RESET}")
            print(f"      {model['description']}")
            print()
    
    print(f"{NEON_CYAN}[0]{RESET} ← Back to main menu\n")
    
    while True:
        choice = input(f"{NEON_PURPLE}Select model (1-{len(AI_MODELS)} or 0): {RESET}").strip()
        
        if choice == "0":
            return None
        elif choice in AI_MODELS:
            model = AI_MODELS[choice]
            print(f"\n{NEON_GREEN}[✓] Selected: {model['name']}{RESET}")
            
            # Show detailed info
            print_box(f"📋 {model['name']} Details", f"""
Type: {model['type']}
Size: {model['size']}
RAM Required: {model['ram_required']}

Use Cases:
{chr(10).join('  • ' + uc for uc in model['use_cases'])}

{model['description']}
""", NEON_CYAN)
            
            confirm = input(f"\n{NEON_YELLOW}Proceed with this model? (y/n): {RESET}").strip().lower()
            if confirm == 'y':
                return choice
        else:
            print(f"{NEON_RED}[!] Invalid selection. Please try again.{RESET}")

def install_additional_model():
    """Install additional models after initial deployment"""
    clear_screen()
    print_banner()
    
    print_box("📥 Install Additional Model", "Add more models to your deployment", NEON_CYAN)
    
    # Check if Docker containers are running
    success, output = run_command("docker ps --filter 'name=ollama' --format '{{.Names}}'", capture_output=True)
    
    if not success or 'ollama' not in output:
        print(f"{NEON_RED}[!] Ollama container is not running!{RESET}")
        print(f"{NEON_YELLOW}[*] Please start the services first:{RESET}")
        print(f"    cd ~/open-webui && docker compose up -d")
        return False
    
    # Show currently installed models
    print(f"\n{NEON_BLUE}[*] Checking installed models...{RESET}")
    success, installed = run_command("docker exec ollama ollama list", capture_output=True)
    
    if success and installed:
        print(f"\n{NEON_GREEN}Currently installed models:{RESET}")
        print(installed)
    
    # Select new model
    selected_model = select_ai_model()
    if not selected_model:
        return False
    
    # Install the model
    model_info = AI_MODELS[selected_model]
    print(f"\n{NEON_PURPLE}[*] Installing {model_info['name']}...{RESET}")
    print(f"{DIM}This may take 5-15 minutes depending on model size{RESET}")
    
    if model_info['model_id'].startswith('hf.co/'):
        pull_cmd = f"docker exec -it ollama ollama pull {model_info['model_id']}"
    else:
        pull_cmd = f"docker exec -it ollama ollama pull {model_info['file']}"
    
    success, _ = run_command(pull_cmd, f"Downloading {model_info['name']}")
    
    if success:
        print(f"\n{NEON_GREEN}[✓] Model installed successfully!{RESET}")
        print(f"{NEON_CYAN}[*] {model_info['name']} is now available in Open WebUI{RESET}")
    else:
        print(f"{NEON_RED}[!] Failed to install model{RESET}")
        return False
    
    return True

def view_models():
    """Display all available models with detailed information"""
    clear_screen()
    print_banner()
    
    print_box("🤖 Available AI Models", "Cybersecurity-Enhanced Collection", NEON_PURPLE)
    
    # Group and display models by category
    categories = {
        'Security': [],
        'Coding': [],
        'Reasoning': [],
        'General': []
    }
    
    for key, model in AI_MODELS.items():
        categories[model['type']].append((key, model))
    
    for category, models in categories.items():
        if models:
            print(f"\n{NEON_CYAN}{BRIGHT}━━━ {category.upper()} MODELS ━━━{RESET}")
            for key, model in models:
                print(f"\n{NEON_GREEN}[{key}] {model['name']}{RESET}")
                print(f"    {DIM}Size: {model['size']} | RAM: {model['ram_required']}{RESET}")
                print(f"    {model['description']}")
                print(f"    {NEON_YELLOW}Use cases:{RESET}")
                for uc in model['use_cases']:
                    print(f"      • {uc}")
    
    input(f"\n{NEON_PURPLE}Press Enter to continue...{RESET}")

def system_status():
    """Check system and service status"""
    clear_screen()
    print_banner()
    
    print_box("📊 System Status", "Checking system health...", NEON_CYAN)
    
    # Check Docker
    print(f"\n{NEON_BLUE}Docker Status:{RESET}")
    success, _ = run_command("systemctl is-active docker", capture_output=True)
    if success:
        print(f"  {NEON_GREEN}[✓] Docker is running{RESET}")
    else:
        print(f"  {NEON_RED}[✗] Docker is not running{RESET}")
    
    # Check containers
    print(f"\n{NEON_BLUE}Container Status:{RESET}")
    run_command("docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'")
    
    # Check installed models
    print(f"\n{NEON_BLUE}Installed Models:{RESET}")
    run_command("docker exec ollama ollama list 2>/dev/null || echo '  No models installed or Ollama not running'")
    
    # Check disk usage
    print(f"\n{NEON_BLUE}Disk Usage:{RESET}")
    run_command("df -h / | tail -1")
    
    # Check memory
    print(f"\n{NEON_BLUE}Memory Usage:{RESET}")
    run_command("free -h | grep Mem")
    
    input(f"\n{NEON_PURPLE}Press Enter to continue...{RESET}")

def learning_resources():
    """Display curated cybersecurity and AI learning resources"""
    clear_screen()
    print_banner()
    
    print_box("🎓 Learning Resources", "Cybersecurity & AI Education", NEON_GREEN)
    
    resources = f"""
{NEON_RED}{BRIGHT}🔐 CYBERSECURITY LEARNING:{RESET}

  {NEON_CYAN}Platforms:{RESET}
    • TryHackMe - https://tryhackme.com
    • HackTheBox - https://hackthebox.com
    • PentesterLab - https://pentesterlab.com
    • PortSwigger Academy - https://portswigger.net/web-security
    
  {NEON_CYAN}Certifications:{RESET}
    • OSCP - Offensive Security Certified Professional
    • CEH - Certified Ethical Hacker
    • CISSP - Certified Information Systems Security Professional
    • CompTIA Security+
    
{NEON_BLUE}{BRIGHT}🤖 AI/ML SECURITY:{RESET}

  {NEON_CYAN}Courses:{RESET}
    • Adversarial ML - https://adversarial-ml-tutorial.org/
    • AI Security - https://aisecure.github.io/
    • ML Security Evasion - https://github.com/13o-bbr-bbq/machine_learning_security
    
  {NEON_CYAN}Tools & Frameworks:{RESET}
    • Adversarial Robustness Toolbox (ART)
    • CleverHans - adversarial examples library
    • SecML - ML security library
    
{NEON_GREEN}{BRIGHT}📚 RECOMMENDED BOOKS:{RESET}
    
  • "The Web Application Hacker's Handbook"
  • "Practical Malware Analysis"
  • "The Art of Software Security Assessment"
  • "Gray Hat Python"
  • "Black Hat Python"
    
{NEON_PURPLE}{BRIGHT}🎯 PRACTICE LABS:{RESET}

  • OWASP WebGoat
  • DVWA (Damn Vulnerable Web Application)
  • Metasploitable
  • VulnHub VMs
  • PicoCTF challenges
"""
    
    print(resources)
    input(f"\n{NEON_PURPLE}Press Enter to continue...{RESET}")

def quick_reference():
    """Display quick command reference"""
    clear_screen()
    print_banner()
    
    print_box("📖 Quick Reference", "Essential commands for your AI system", NEON_CYAN)
    
    commands = f"""
{NEON_GREEN}{BRIGHT}DOCKER COMMANDS:{RESET}
  docker ps                      # List running containers
  docker logs ollama            # View Ollama logs
  docker logs open-webui        # View Open WebUI logs
  docker stats                  # Monitor resource usage
  docker system prune -a        # Clean up unused resources

{NEON_BLUE}{BRIGHT}SERVICE MANAGEMENT:{RESET}
  cd ~/open-webui
  docker compose up -d          # Start services
  docker compose down           # Stop services
  docker compose restart        # Restart services
  docker compose logs -f        # Follow logs

{NEON_PURPLE}{BRIGHT}MODEL MANAGEMENT:{RESET}
  docker exec ollama ollama list                    # List models
  docker exec -it ollama ollama pull MODEL_NAME     # Install model
  docker exec ollama ollama rm MODEL_NAME           # Remove model
  docker exec -it ollama ollama run MODEL_NAME      # Test model

{NEON_YELLOW}{BRIGHT}SECURITY HARDENING:{RESET}
  ufw allow 22/tcp              # Allow SSH
  ufw allow 3000/tcp            # Allow Open WebUI
  ufw enable                    # Enable firewall
  fail2ban-client status        # Check fail2ban
  
{NEON_RED}{BRIGHT}TROUBLESHOOTING:{RESET}
  systemctl status docker       # Check Docker status
  systemctl restart docker      # Restart Docker
  docker compose down && docker compose up -d  # Full restart
  docker exec -it ollama /bin/bash            # Shell into Ollama
  journalctl -u docker -f      # View Docker logs
"""
    
    print(commands)
    input(f"\n{NEON_PURPLE}Press Enter to continue...{RESET}")

def interactive_menu():
    """Main interactive menu"""
    while True:
        clear_screen()
        print_banner()
        
        menu_options = f"""
{NEON_CYAN}{BRIGHT}🎮 MAIN MENU - Choose Your Action{RESET}

  {NEON_GREEN}[1]{RESET} 🚀 Deploy AI System
  {NEON_GREEN}[2]{RESET} 🤖 View AI Models  
  {NEON_GREEN}[3]{RESET} 📥 Install Additional Model
  {NEON_GREEN}[4]{RESET} 🎓 Learning Resources
  {NEON_GREEN}[5]{RESET} 📊 System Status
  {NEON_GREEN}[6]{RESET} 📖 Quick Reference
  {NEON_GREEN}[7]{RESET} 👋 Exit

"""
        print(menu_options)
        
        choice = input(f"{NEON_PURPLE}Select option (1-7): {RESET}").strip()
        
        if choice == "1":
            deploy_ai_system()
            input(f"\n{NEON_PURPLE}Press Enter to continue...{RESET}")
        elif choice == "2":
            view_models()
        elif choice == "3":
            install_additional_model()
            input(f"\n{NEON_PURPLE}Press Enter to continue...{RESET}")
        elif choice == "4":
            learning_resources()
        elif choice == "5":
            system_status()
        elif choice == "6":
            quick_reference()
        elif choice == "7":
            print(f"\n{NEON_CYAN}[*] Exiting... Stay secure! 🔐{RESET}")
            sys.exit(0)
        else:
            print(f"{NEON_RED}[!] Invalid option. Please try again.{RESET}")
            time.sleep(2)

def main():
    """Main entry point"""
    try:
        # Check if running as root (recommended for Docker installation)
        if os.geteuid() != 0:
            print(f"{NEON_YELLOW}[!] Warning: Not running as root. Some operations may require sudo.{RESET}")
            print(f"{NEON_CYAN}[*] Consider running with: sudo python3 {sys.argv[0]}{RESET}")
            time.sleep(3)
        
        # Start interactive menu
        interactive_menu()
        
    except KeyboardInterrupt:
        print(f"\n\n{NEON_RED}[!] Installation cancelled by user{RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{NEON_RED}[!] An error occurred: {e}{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()

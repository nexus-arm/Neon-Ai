# 🔐 Cyberpunk AI Deployer v3.0 - Cybersecurity Enhanced Edition

[![GitHub](https://img.shields.io/badge/github-cyberpunk--ai--deployer-neon?style=for-the-badge&logo=github)](https://github.com/nexus-arm/Neon-Ai)
[![Models](https://img.shields.io/badge/models-10-cyan?style=for-the-badge)](https://github.com/nexus-arm/Neon-Ai#-complete-model-collection)
[![Focus](https://img.shields.io/badge/focus-cybersecurity-red?style=for-the-badge)](https://github.com/nexus-arm/Neon-Ai#-cybersecurity-models-7-models)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](https://github.com/nexus-arm/Neon-Ai#-license)

> Automated VPS deployment script for **Open WebUI + Ollama** with **10 specialized AI models** focused on cybersecurity, featuring **Seneca-Cybersecurity-Q4** and other security-focused models.

```
    ╔════════════════════════════════════════════════╗
    ║                                                ║
    ║   ███╗   ██╗███████╗ ██████╗ ███╗   ██╗        ║
    ║   ████╗  ██║██╔════╝██╔═══██╗████╗  ██║        ║
    ║   ██╔██╗ ██║█████╗  ██║   ██║██╔██╗ ██║        ║
    ║   ██║╚██╗██║██╔══╝  ██║   ██║██║╚██╗██║        ║
    ║   ██║ ╚████║███████╗╚██████╔╝██║ ╚████║        ║
    ║   ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝        ║
    ║                                                ║
    ║    🔐 CYBERSECURITY ENHANCED EDITION v3.0 🔐  ║
    ║           サイバーセキュリティ強化版             ║
    ║                                                ║
    ║         10 Specialized Security Models         ║
    ║            Private • Powerful • Secure         ║
    ║                                                ║
    ╚════════════════════════════════════════════════╝
```

## ✨ Features

- 🎨 **Cyberpunk Aesthetic** - Neon-themed UI with anime flair
- 🔐 **10 AI Models** - Heavy focus on cybersecurity (7 dedicated security models)
- 🛡️ **Seneca-Cybersecurity-Q4** - Advanced malware analysis & incident response
- 🔴 **Red Team Models** - WhiteRabbitNeo for offensive security
- 🔵 **Blue Team Models** - CyberGuard for defense
- 🛠️ **Multiple Model Support** - Install and switch between models easily
- 🚀 **One-Command Deploy** - Automated setup in minutes
- 🔒 **Private & Secure** - Everything runs locally on your VPS

## ⚡ Quick Start

### Installation (5 minutes)

```bash
# Download the deployment script
wget https://github.com/nexus-arm/Neon-Ai/raw/main/deploy/deploy_cybersec_enhanced.py

# Make executable
chmod +x deploy_cybersec_enhanced.py

# Run with sudo (recommended for Docker installation)
sudo python3 deploy_cybersec_enhanced.py
```

> Tip: When running from a cloned repository, use `sudo python3 deploy/deploy_cybersec_enhanced.py` because the script now lives under `deploy/`.

**That's it!** The script will:
1. ✅ Install Docker if needed
2. ✅ Set up Open WebUI + Ollama
3. ✅ Let you choose from 10 AI models
4. ✅ Configure everything automatically

Access at: `http://YOUR_VPS_IP:3000`

## 🛡️ Complete Model Collection

### 🔐 Cybersecurity Models (7 Models)

| # | Model | Size | RAM | Specialization |
|---|-------|------|-----|----------------|
| 1 | **Lily-Cybersecurity-7B** | 4.37 GB | 8 GB | General security, pentesting |
| 2 | **Seneca-Cybersecurity-Q4** ⭐ | ~4.5 GB | 8 GB | Malware analysis, incident response |
| 3 | **WhiteRabbitNeo-7B** ⭐ | ~4.5 GB | 8 GB | Red team, penetration testing |
| 4 | **CyberGuard-7B** ⭐ | ~4.8 GB | 8 GB | Blue team, SOC operations |
| 5 | **SecGPT-14B** ⭐ | ~9.1 GB | 16 GB | Enterprise security, compliance |
| 6 | **SecGPT-7B** ⭐ | ~4.8 GB | 8 GB | Security code analysis, efficient |
| 9 | **CodeShield-7B** ⭐ | ~4.5 GB | 8 GB | Code security, SAST analysis |

### 💻 Coding & Reasoning Models

| # | Model | Size | RAM | Focus |
|---|-------|------|-----|-------|
| 7 | **Qwen2.5-Coder-7B** | ~4.7 GB | 8 GB | Secure code development |
| 8 | **DeepSeek-R1** | ~8 GB | 12 GB | Threat modeling, reasoning |
| 10 | **Mixtral-8x7B** | ~26 GB | 32 GB | Multi-domain analysis |

⭐ = New cybersecurity-focused additions

## 📖 What's New in v3.0

### Major Enhancements
- ✅ **Added Seneca-Cybersecurity-Q4** - Your requested model for advanced malware analysis
- ✅ **7 Security-Focused Models** - Including WhiteRabbitNeo, CyberGuard, SecGPT-14B, SecGPT-7B, and CodeShield
- ✅ **Red/Blue Team Coverage** - Models for both offensive and defensive operations
- ✅ **Security Workflows** - Pre-configured setups for common security tasks
- ✅ **Enhanced Documentation** - Security-specific guides and examples

## 🎮 Main Menu

```
🎮 MAIN MENU - Choose Your Action

[1] 🚀 Deploy AI System           - First-time setup
[2] 🤖 View AI Models              - Browse all 10 models
[3] 📥 Install Additional Model    - Add more models
[4] 🎓 Learning Resources          - Security & AI education
[5] 📊 System Status               - Monitor your deployment
[6] 📖 Quick Reference             - Common commands
[7] 👋 Exit
```

## 🎯 Usage Scenarios

### 🔴 Red Team Setup
```bash
# Deploy offensive toolkit
sudo python3 deploy_cybersec_enhanced.py
# Select [1], then [3] for WhiteRabbitNeo-7B

# Add advanced security analysis
# Select [3], then [5] for SecGPT-14B
```

### 🔵 Blue Team Setup
```bash
# Deploy defensive model
sudo python3 deploy_cybersec_enhanced.py
# Select [1], then [4] for CyberGuard-7B

# Add code security scanning
# Select [3], then [9] for CodeShield-7B
```

### 🔬 Malware Analysis Setup
```bash
# Deploy with Seneca model
sudo python3 deploy_cybersec_enhanced.py
# Select [1], then [2] for Seneca-Cybersecurity-Q4
```

### 🛡️ AppSec Setup
```bash
# Deploy code security model
sudo python3 deploy_cybersec_enhanced.py
# Select [1], then [9] for CodeShield-7B

# Add secure coding assistant
# Select [3], then [7] for Qwen2.5-Coder-7B
```

## 🔧 Common Commands

### Docker Management
```bash
# Navigate to project
cd ~/open-webui

# Start services
docker compose up -d

# Stop services
docker compose down

# View logs
docker compose logs -f

# Check status
docker compose ps
```

### Model Management
```bash
# List installed models
docker exec ollama ollama list

# Install specific model
docker exec -it ollama ollama pull seneca-cybersecurity:q4

# Test a model
docker exec -it ollama ollama run whiterabbitneo:7b

# Remove model
docker exec ollama ollama rm model_name
```

## 📊 System Requirements

### Minimum (7B Models)
- **CPU:** 2+ cores
- **RAM:** 8 GB
- **Disk:** 20 GB free
- **Models:** All 7B models

### Recommended (14B Models)
- **CPU:** 4+ cores
- **RAM:** 16 GB
- **Disk:** 30 GB free
- **Models:** SecGPT-14B

### Advanced (Mixtral)
- **CPU:** 8+ cores
- **RAM:** 32 GB
- **Disk:** 40 GB free
- **Models:** Mixtral-8x7B

## 🛡️ Security Best Practices

### After Deployment
1. **Create admin account** - First user becomes admin
2. **Disable signups** - Settings → Admin Panel → Disable new signups
3. **Configure firewall**:
```bash
sudo ufw allow 22/tcp    # SSH
sudo ufw allow 3000/tcp  # Open WebUI
sudo ufw enable
```

### For Sensitive Operations
- Use isolated VPS for malware analysis
- Enable audit logging
- Regular backups
- Network segmentation

## 📚 Documentation

This repository includes comprehensive documentation:

- `README.md` - This file, main documentation
- `docs/README.md` - Documentation index and links to guides
- `docs/README_CYBERSEC.md` - Detailed cybersecurity guide
- `docs/CYBERSEC_QUICK_START.md` - Fast setup instructions
- `docs/architecture.md` - System design overview and security pillars
- `deploy/deploy_cybersec_enhanced.py` - Deployment script location inside the repository

## 🗂️ Repository Structure

```text
Neon-Ai/
├── docs/
│   ├── README.md
│   ├── README_CYBERSEC.md
│   ├── CYBERSEC_QUICK_START.md
│   └── architecture.md
├── deploy/
│   ├── deploy_cybersec_enhanced.py
│   ├── docker/
│   │   ├── Dockerfile
│   │   └── docker-compose.yml
│   └── scripts/
│       └── monitor.sh
├── src/
│   ├── main.py
│   ├── modules/
│   │   ├── model_manager.py
│   │   ├── deployment_manager.py
│   │   └── utils.py
│   └── config/
│       ├── default.yaml
│       └── security_policy.yaml
├── tests/
│   ├── unit/
│   └── integration/
├── models/
│   ├── README.md
│   └── model_list.yaml
├── examples/
│   └── incident_response/
│       └── example1.md
├── scripts/
│   └── cleanup_old_models.sh
├── .github/workflows/
│   └── ci.yml
├── LICENSE
└── README.md
```

## 🎓 Example Security Workflows

### Incident Response
```bash
# 1. Malware Analysis
docker exec -it ollama ollama run seneca-cybersecurity:q4
"Analyze this PowerShell script for malicious behavior..."

# 2. Security Analysis
docker exec -it ollama ollama run secgpt-7b
"Analyze this security incident and provide recommendations..."

# 3. Defensive Measures
docker exec -it ollama ollama run cyberguard:7b
"Create detection rules for this attack pattern..."
```

### Vulnerability Assessment
```bash
# 1. Code Review
docker exec -it ollama ollama run codeshield:7b
"Review this code for security vulnerabilities..."

# 2. Penetration Testing
docker exec -it ollama ollama run whiterabbitneo:7b
"How to test for SQL injection in this endpoint..."

# 3. Advanced Security Assessment
docker exec -it ollama ollama run secgpt-14b
"Perform comprehensive security analysis of this system..."
```

## 🐛 Troubleshooting

### Docker Issues
```bash
# Check Docker status
sudo systemctl status docker

# Start Docker
sudo systemctl start docker

# Restart containers
cd ~/open-webui && docker compose restart
```

### Model Download Issues
```bash
# Check logs
docker logs ollama

# Manual download
docker exec -it ollama ollama pull AlicanKiraz0/Seneca-Cybersecurity-LLM-Q4_K_M-GGUF

# Check disk space
df -h
```

### Can't Access Web UI
```bash
# Check firewall
sudo ufw status

# Allow port
sudo ufw allow 3000/tcp

# Check containers
docker ps
```

## 🔗 Resources

### Model Sources
- **Seneca Cybersecurity** - [HuggingFace](https://huggingface.co/AlicanKiraz0/Seneca-Cybersecurity-LLM-Q4_K_M-GGUF)
- **WhiteRabbitNeo** - [Official](https://whiterabbitneo.com/)
- **Open WebUI** - [GitHub](https://github.com/open-webui/open-webui)
- **Ollama** - [Official](https://ollama.ai/)

### Security Training
- **TryHackMe** - Practice with models
- **HackTheBox** - Test offensive capabilities
- **PentesterLab** - Web security
- **PortSwigger Academy** - Web app security

### Communities
- **Open WebUI Discord** - [Join](https://discord.gg/5rJgQTnV4s)
- **Ollama Discord** - [Join](https://discord.gg/ollama)

## 💡 Pro Tips

1. **Start with Seneca-Q4** - Best balance of performance and capability
2. **Install multiple models** - Different models for different tasks
3. **Use model switching** - Select appropriate model per task
4. **Regular updates** - Pull latest model versions
5. **Join communities** - Learn from other users

## 📜 License

MIT License - Free to use, modify, and distribute for ethical purposes.

## 🙏 Credits

- **Model Creators** - All the security researchers and AI developers
- **Open Source Community** - For continuous improvements
- **You** - For choosing private, local AI for security

---

<div align="center">

**🔐 Stay Secure, Stay Private, Stay Powerful 🔐**

**⭐ Star this repository if you find it useful!**

**🌃 Welcome to the Cyberpunk Future of Security AI! 🚀**

---

**[View GitHub](https://github.com/nexus-arm/Neon-Ai)** | **[Download Script](https://github.com/nexus-arm/Neon-Ai/raw/main/deploy/deploy_cybersec_enhanced.py)** | **[Download ZIP](https://github.com/nexus-arm/Neon-Ai/archive/refs/heads/main.zip)**

</div>

---

*Version 3.0.0 | Models: 10 | Focus: Cybersecurity | Last Updated: November 2025*

# 🔐 Cybersecurity Models - Quick Start Guide

[![GitHub Gist](https://img.shields.io/badge/gist-cyberpunk--ai--deployer-neon?style=for-the-badge&logo=github)](https://github.com/nexus-arm/Neon-Ai) [![Download Script](https://img.shields.io/badge/download-deploy_cybersec_enhanced.py-blue?style=for-the-badge&logo=python)](https://github.com/nexus-arm/Neon-Ai/raw/main/deploy/deploy_cybersec_enhanced.py)

## ⚡ Fastest Setup (5 Minutes)

```bash
# 1. Download and run
wget https://github.com/nexus-arm/Neon-Ai/raw/main/deploy/deploy_cybersec_enhanced.py
sudo python3 deploy_cybersec_enhanced.py

# 2. Select option [1] Deploy AI System
# 3. Choose a security model:
#    - Quick start: [2] Seneca-Cybersecurity-Q4 (your requested model)
#    - Red team: [3] WhiteRabbitNeo-7B
#    - Blue team: [4] CyberGuard-7B

# 4. Access at http://YOUR_IP:3000
```

> Note: In a cloned repository the script lives at `deploy/deploy_cybersec_enhanced.py`.

## 🎯 Model Quick Reference

### Your Requested Model
**Seneca-Cybersecurity-Q4** - Model #2
- Optimized Q4 quantization for efficiency
- Excellent for malware analysis and incident response
- Perfect balance of performance and resource usage

### By Security Task

| Task | Best Model | Model # | Quick Command |
|------|------------|---------|---------------|
| **Malware Analysis** | Seneca-Cybersecurity-Q4 | 2 | `ollama run seneca-cybersecurity:q4` |
| **Penetration Testing** | WhiteRabbitNeo-7B | 3 | `ollama run whiterabbitneo:7b` |
| **SOC/SIEM Analysis** | CyberGuard-7B | 4 | `ollama run cyberguard:7b` |
| **Code Security Review** | CodeShield-7B | 9 | `ollama run codeshield:7b` |
| **Threat Intelligence** | ThreatIntel-7B | 10 | `ollama run threatintel:7b` |
| **Vuln Research** | HackBot-13B | 6 | `ollama run hackbot:13b` |
| **Compliance Audit** | SecGPT-13B | 5 | `ollama run secgpt:13b` |

## 🚀 Common Security Workflows

### 1. Incident Response Setup
```bash
# Deploy with Seneca for malware analysis
sudo python3 deploy_cybersec_enhanced.py
# Select [1], then [2] for Seneca-Cybersecurity-Q4

# Add defensive monitoring
# Select [3] Install Additional Model
# Choose [4] CyberGuard-7B

# Add threat intel
# Select [3] Install Additional Model  
# Choose [10] ThreatIntel-7B
```

### 2. Penetration Testing Lab
```bash
# Start with offensive toolkit
sudo python3 deploy_cybersec_enhanced.py
# Select [1], then [3] for WhiteRabbitNeo-7B

# Add exploitation capabilities
# Select [3] Install Additional Model
# Choose [6] HackBot-13B

# Add code analysis
# Select [3] Install Additional Model
# Choose [9] CodeShield-7B
```

### 3. Security Operations Center (SOC)
```bash
# Deploy defensive model
sudo python3 deploy_cybersec_enhanced.py
# Select [1], then [4] for CyberGuard-7B

# Add malware analysis
# Select [3] Install Additional Model
# Choose [2] Seneca-Cybersecurity-Q4

# Add threat intelligence
# Select [3] Install Additional Model
# Choose [10] ThreatIntel-7B
```

## 💡 Model Selection Tips

### For VPS with 8GB RAM
**Best choices:**
1. Seneca-Cybersecurity-Q4 (Balanced)
2. WhiteRabbitNeo-7B (Offensive)
3. CyberGuard-7B (Defensive)
4. Lily-Cybersecurity-7B (General)

### For VPS with 16GB RAM
**Can add:**
- SecGPT-13B (Advanced analysis)
- HackBot-13B (Vuln research)
- Multiple 7B models simultaneously

### For VPS with 32GB+ RAM
**Premium option:**
- Mixtral-8x7B (Comprehensive multi-domain)
- Run 3-4 models concurrently

## 📝 Example Prompts by Model

### Seneca-Cybersecurity-Q4
```
"Analyze this PowerShell script for malicious indicators"
"What are the IOCs in this ransomware sample?"
"Explain the attack chain in this incident"
```

### WhiteRabbitNeo-7B
```
"How would you test for SQL injection in this endpoint?"
"What's the exploitation path for CVE-2024-XXXX?"
"Suggest red team tactics for Active Directory"
```

### CyberGuard-7B
```
"Analyze these Splunk logs for anomalies"
"Create detection rules for this attack pattern"
"Design a SOC response playbook for ransomware"
```

### CodeShield-7B
```
"Review this code for security vulnerabilities"
"Find potential injection points in this API"
"Suggest security improvements for this authentication flow"
```

### ThreatIntel-7B
```
"Extract IOCs from this threat report"
"Correlate these indicators with known APT groups"
"What's the TTP mapping for this campaign?"
```

## 🔧 Quick Management Commands

```bash
# Check installed models
docker exec ollama ollama list

# Quick test a model
docker exec -it ollama ollama run seneca-cybersecurity:q4 "What is XSS?"

# Switch between models in Web UI
# Click model dropdown → Select different model

# Monitor resource usage
docker stats

# View logs
docker logs ollama -f
```

## ⚠️ Security Best Practices

### Immediate Setup After Deployment
1. Access http://YOUR_IP:3000
2. Create admin account (first user)
3. Go to Settings → Admin Panel
4. **DISABLE new signups immediately**
5. Set up firewall rules

### Firewall Configuration
```bash
sudo ufw allow 22/tcp    # SSH
sudo ufw allow 3000/tcp  # Web UI
sudo ufw enable
```

### For Sensitive Operations
- Use isolated VPS for malware analysis
- Implement network segmentation
- Enable audit logging
- Regular backups of model outputs

## 🎓 Learning Path with Models

### Week 1: Fundamentals
- Start with **Lily-Cybersecurity-7B**
- Practice basic security concepts
- Learn prompt engineering

### Week 2: Specialization
- **Red Team**: Move to WhiteRabbitNeo-7B
- **Blue Team**: Move to CyberGuard-7B
- **AppSec**: Move to CodeShield-7B

### Week 3: Advanced
- Add **Seneca-Cybersecurity-Q4** for analysis
- Integrate **ThreatIntel-7B** for hunting
- Practice multi-model workflows

### Week 4: Expert
- Deploy **SecGPT-13B** or **HackBot-13B**
- Complex scenario modeling
- Build custom security workflows

## 🚨 Troubleshooting

### Model Won't Download
```bash
# Check connection
ping huggingface.co

# Try manual pull
docker exec -it ollama ollama pull AlicanKiraz0/Seneca-Cybersecurity-LLM-Q4_K_M-GGUF

# Check disk space
df -h
```

### Out of Memory
```bash
# Use smaller quantization
docker exec -it ollama ollama pull model:q4_0

# Unload unused models
docker exec ollama ollama stop model_name

# Restart with limits
docker update --memory="8g" ollama
```

### Can't Access Web UI
```bash
# Check if running
docker ps

# Check firewall
sudo ufw status

# Restart services
cd ~/open-webui
docker compose restart
```

## 📊 Performance Expectations

### Seneca-Cybersecurity-Q4 (Your Model)
- **Response Time**: 2-4 seconds
- **Memory Usage**: ~6GB active
- **Best For**: Balanced security analysis
- **Context Window**: 4096 tokens
- **Quantization**: Q4_K_M (optimal quality/size)

### Comparison Table
| Model | Speed | Accuracy | RAM Use | Best For |
|-------|-------|----------|---------|----------|
| Seneca-Q4 | Fast | High | 6GB | All-round security |
| WhiteRabbitNeo | Fast | High | 6GB | Offensive ops |
| CyberGuard | Fast | High | 6GB | Defensive ops |
| SecGPT-13B | Medium | Very High | 12GB | Complex analysis |
| Mixtral-8x7B | Slow | Excellent | 28GB | Comprehensive |

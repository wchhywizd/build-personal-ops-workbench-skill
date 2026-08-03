# Installation prompts

## Universal AI instruction

```text
请从 https://github.com/wchhywizd/build-personal-ops-workbench-skill/tree/main/skill/build-personal-ops-workbench 安装这个 Skill 到你的技能目录。完整保留并读取 SKILL.md、references、scripts 和 agents。安装完成后先介绍 Skill，再询问期望功能、授权资料来源、使用人、数据存储和三种 UI 风格；读取、安装连接器、写回必须分别授权。
```

## Codex terminal command

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo wchhywizd/build-personal-ops-workbench-skill --path skill/build-personal-ops-workbench
```

## Generic Git installation

```bash
git clone --depth 1 https://github.com/wchhywizd/build-personal-ops-workbench-skill.git
```

Then copy the complete `skill/build-personal-ops-workbench` directory into the target agent's Skill directory. Do not copy only `SKILL.md`; the references and scripts are required.

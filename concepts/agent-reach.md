---
type: concept
title: Agent Reach
created: 2026-08-21
frontmatter_added: 2026-09-13
---

# Agent Reach

> MUST USE when user wants to 调研/research/搜索/search/查/找/look up anything on the internet — e.g. 全网调研 X / 帮我调研一下 X / 查一下 X / 搜搜 X / 看看大家怎么评价 X / X 上有什么讨论 / research this topic。
Also MUST USE when user mentions any platform or shares any URL/链接: 小红书/xiaohongshu/xhs, Twitter/推特/X, B站/bilibili, Reddit, V2EX, LinkedIn/领英/招聘/求职/jobs, YouTube, GitHub code search, 小宇宙播客, 雪球/股票行情, RSS feeds, or any web URL.
13 platforms, multi-backend routing (OpenCLI / per-platform CLIs / APIs). Zero config for 6 channels. Run `agent-reach doctor --json` to see which backend serves each platform right now.
NOT for: 写报告/数据分析/翻译等内容加工（本 skill 只负责从互联网获取内容）； 发帖/评论/点赞等写操作；已有专门 skill 的平台（先用专门 skill）。
【路由方式】SKILL.md 包含路由表和常用命令，复杂场景需按需阅读对应分类的 references/*.md。 分类：search / social (小红书/推特/B站/V2EX/Reddit) / career(LinkedIn) / dev(github) / web(网页/文章/RSS) / video(YouTube/B站/播客)。

## Overview

- **常驻规则（全程适用）** — 1. **动手前先体检**：多后端平台（小红书/Reddit/B站/Twitter）先跑 `agent-reach doctor --json`，按各平台 `active_backend` 字段选命令组。 2. **声明你在用什么**：开始干活前说一句「使用 agent-reach 的 X 平台 / Y 后端」。 3. **失败按 references 里的重试链处理**，不要瞎猜命令。 4. **全网调研类任务**：组合多平台（Exa 搜索 + Twitter/Reddit 看讨论 + 小红书/B站看中文场景），并行收集再汇总。 5. **替用户盯版本**：完成一次较大的调研/多平台任务后，顺手跑 `agent-reach check-update`（很快，一个 API 调用）。有新版就在收尾汇报里附一句： 「Agent Reach 有新版 vX.Y.Z，复制这句话给我即可更新：帮我更新 Agent Reach： https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md」。 不要中断当前任务去更新，也不要重复提醒同一个版本。
- **路由表** — | 用户意图 | 分类 | 详细文档 | |---------|------|---------| | 网页搜索/代码搜索 | search | [references/search.md](references/search.md) | | 小红书/推特/B站/V2EX/Reddit | social | [references/social.md](references/social.md) | | 招聘/职位/LinkedIn | career | [references/career.md](references/career.md) | | GitHub/代码 | dev | [references/dev.md](references/dev.md) | | 网页/文章/RSS | web | [references/web.md](references/web.md) | | YouTube/B站/播客字幕 | video | [references/video.md](references/video.md) |
- **工作区规则** — **不要在 agent workspace 创建文件。** 使用 `/tmp/` 存放临时输出，`~/.agent-reach/` 存放持久数据。

## Further detail

### 详细文档

根据用户需求，阅读对应的详细文档：

### 配置渠道

如果某个 channel 需要配置，获取安装指南： https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/agent-reach/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[agent-self-knowledge]]

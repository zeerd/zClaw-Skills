# 🔧 全人描述提示词模板库

本目录下提供了完整的全人描述提示词模板和示例。

---

## 🗂️ 模板目录

- [`face-body-combo.md`](face-body-combo.md) - 面部 + 身体组合模板
- [`criminal-profile.md`](criminal-profile.md) - 刑侦嫌疑人描述模板
- [`character-design.md`](character-design.md) - 游戏/影视角色设计模板
- [`realistic-portrait.md`](realistic-portrait.md) - 写实风格全身肖像模板
- [`stylized-character.md`](stylized-character.md) - 风格化角色设计模板

---

## 📋 所有模板总览

### 模板 1: 基础全人描述

```markdown
[性别], [年龄], [体型分类], [身高],
[肩部特征], [胸廓特征], [四肢比例],
[站姿], [手部习惯], [步态],
[上装 + 合身度 + 状态],
[下装 + 合身度 + 状态],
[鞋履/配饰],
[环境], [镜头], [质量]
```

### 模板 2: 刑侦嫌疑人风格

```markdown
Subject: [基本身份信息]
Posture: [站姿 + 手部习惯], [步态描述]
Attire: [上装具体描述], [下装具体描述], [鞋履/配饰]
Style: [整体风格关键词]
Environment: [环境背景]
Camera: [拍摄角度 + 镜头 + 质量]
```

### 模板 3: 角色设计风格

```markdown
Character: [姓名/代号], [性别], [年龄], [体型特征]
Physical: [骨架细节], [身姿特征]
Outfit: [服装组合], [风格定位]
Personality: [通过姿态表达的个性]
Setting: [角色所处环境]
Rendering: [渲染风格]
```

---

## 🎯 模板使用指南

### 模板变体技巧

**调整风格**:
```markdown
# 将写实改为卡通风格
写实：photorealistic, 8k, detailed skin texture
卡通：stylized, cartoon style, simplified features
```

**调整年代**:
```markdown
# 将现代改为复古风格
现代：smartwatch, denim jeans, sneakers
复古：fedora hat, tweed suit, leather dress shoes
```

**调整环境**:
```markdown
# 添加特定环境特征
城市：urban street, concrete, neon lights
自然：forest background, natural lighting, dirt path
室内：office setting, desk, bookshelf
```

---

## 📦 配套参数库

### 体型分类参数

```markdown
# 外胚层 (瘦长)
Ectomorph: lean and linear, narrow shoulders and hips, low body fat, long limbs

# 中胚层 (运动)
Mesomorph: athletic build, broad shoulders, narrow waist, muscular definition

# 内胚层 (圆润)
Endomorph: soft and round, wide waist, thick neck, heavy lower body

# 混合类型
Mesomorph with endomorphic tendencies: muscular build with slight belly
```

### 身高量级参数

```markdown
# 绝对高度
175cm tall, 185cm tall, 160cm tall (petite), 190cm tall (towering)

# 相对描述
average height for male, average height for female
tall for her age, short and stocky
```

### 步态特征参数

```markdown
# 速度
brisk walk, slow shuffling gait, leisurely pace

# 特殊步态
limping on right leg, swaggering walk, dragging feet
duck-footed (toes point outward), knees knock together

# 节奏
long strides, short quick steps, steady rhythm
```

### 服装合身度参数

```markdown
# 宽松
oversized clothing, baggy jeans, loose fit, hanging loosely

# 紧身
tight-fitting shirt, skinny jeans, clothes straining at buttons

# 不合身
ill-fitting suit, sleeves too long, worn-out shoes

# 状态
wrinkled shirt, stained collar, frayed cuffs, polished shoes, muddy boots
```

---

## 🔄 一致性技巧

### 锚点特征法

每个角色需要 2-3 个**锚点特征**:

```markdown
Anchor 1: Square broad shoulders
Anchor 2: Hands always in pockets
Anchor 3: Worn white sneakers
```

### 分层生成策略

```markdown
# 第一步：生成全身（确定身材、姿势、衣着）
Subject: Male, athletic build, tall
Posture: Standing straight, arms crossed
Outfit: Black t-shirt, blue jeans, sneakers

# 第二步：重绘面部（精细化）
Focus: Face area only
Details: Specific facial features, expression
```

### 不完美法则

```markdown
# 增加真实感的"缺陷"
- Slight belly bulge (肚子微凸)
- Wrinkled shirt (衣服皱巴巴)
- Loose shoelaces (鞋带散了)
- Faded jeans (褪色牛仔裤)
- Scuffed boots (磨损的靴子)
```

---

## 🚀 从描述到提示词转化流程

### Step 1: 观察记录

```markdown
观察到的特征：
- 身高约 180cm，体型中等偏壮
- 肩宽，站姿挺拔
- 穿黑色连帽衫，灰色运动裤
- 走路速度快，双手插兜
```

### Step 2: 参数映射

```markdown
将观察转化为结构化参数：
身高/体型：180cm tall, mesomorph athletic build
肩部：square broad shoulders
站姿：standing straight, confident posture
手部：hands in pockets
上装：tight-fitting black hoodie
下装：loose gray sweatpants
步态：brisk walk
```

### Step 3: 提示词生成

```markdown
male, 30s, mesomorph athletic build, 180cm tall,
square broad shoulders, standing straight, confident posture,
hands in pockets,
tight-fitting black hoodie, loose gray sweatpants,
brisk walk,
urban street background, low angle shot,
35mm lens, realistic texture, 8k
```

---

## 📚 高级技巧

### 镜头语言运用

```markdown
# 强调身高
low angle shot (仰拍), wide angle lens

# 强调细节
close-up shot, 50mm lens, bokeh

# 强调氛围
wide shot, establishing shot, atmospheric lighting
```

### 光影风格

```markdown
# 写实风格
natural lighting, softbox lighting, golden hour

# 戏剧风格
dramatic lighting, low key lighting, chiaroscuro

# 环境光
streetlight glow, neon lights, candlelight
```

---
name: zclaw-full-body-profiling
description: >
  全人描述法/全人画像技能。构建完整的嫌疑人或角色档案，包括面部、体态和动态/衣着特征。
  这个技能就是用来帮你把一个人从头到脚、从外到内都描述得很详细。不只是长什么样子，还包括他的身高体型、站姿走路的样子、穿什么衣服、甚至有没有什么特别的小动作。无论是要画嫌疑人画像，还是设计游戏、影视里的角色，都能用这个方法把人物形象立体、真实地展现出来。
---

# 🧍 全人描述法 (Full-Body Profiling) - 技能说明

## 技能概述

这是一个专业的人体全方位描述技能，用于：

1. **刑侦模拟画像**：为嫌疑人或目击者提供完整的人物描述
2. **高级 AIGC 生成**：创建高度一致性和真实感的角色
3. **游戏/影视角色设计**：构建立体的虚拟角色档案

核心方法论：**由内而外、由静到动**的三维立体描述模型 (3D Profiling Model)

同时提供中英文两个版本。

---

## 📊 三维立体描述模型

### 第一维度：静态骨架与体量 (The Static Frame)

**目标**：确定人物的物理边界和比例，这是身份一致性的基础锚点。

#### 1. 身高与量级 (Height & Stature)

| 描述类型 | 选项示例 | 说明 |
|---------|---------|------|
| 绝对高度 | `185cm tall`, `petite (approx. 155cm)` | 具体身高数值 |
| 相对比例 | `towering over the crowd`, `average height for a male` | 与他人的比较 |
| 体量感 | `heavy-set`, `slender build`, `stocky`, `lanky` | 整体体型 |

#### 2. 体型分类 (Somatotype - 谢尔顿体型分类法)

| 体型类型 | 英文描述 | 特征 |
|---------|---------|------|
| **外胚层 (Ectomorph)** | `lean and linear` | 瘦长型 - 窄肩窄臀，体脂低，四肢修长 |
| **中胚层 (Mesomorph)** | `athletic build` | 运动型/倒三角 - 宽肩窄腰，肌肉明显 |
| **内胚层 (Endomorph)** | `soft and round` | 圆润型 - 宽腰粗颈，下肢沉重 |
| **混合描述** | `mesomorph with endomorphic tendencies` | 肌肉型但有肚腩 |

#### 3. 局部骨骼特征 (Skeletal Landmarks)

即使穿宽松衣服也能识别的特征：

- **肩宽**: `sloping shoulders` (溜肩) / `square broad shoulders` (平宽肩)
- **胸廓**: `barrel chest` (桶状胸) / `pigeon chest` (鸡胸) / `flat chest`
- **脊柱**: `slight hunchback` (微驼背) / `swayback` (骨盆前倾)
- **四肢比例**: `long arms relative to torso` / `short legs` / `thick calves`

💡 **AIGC 提示词技巧**: 使用 `full body shot`, `standing straight`, `neutral pose` 来固定这些特征。

---

### 第二维度：动态身姿与步态 (Dynamic Posture & Gait)

**目标**：捕捉人物的"气质"和习惯性动作，让人物"活"起来。

#### 1. 静态站姿 (Standing Posture)

| 参数类别 | 选项示例 |
|---------|---------|
| 重心分布 | `weight shifted to left leg`, `balanced stance` |
| 脊柱形态 | `upright and rigid` (挺拔僵硬) / `slouched forward` (含胸驼背) / `leaning back casually` |
| 手部习惯 | `hands in pockets`, `arms crossed tightly`, `fidgeting hands`, `clenched fists` |
| 头部姿态 | `chin up` (傲慢) / `head down` (顺从) / `tilted head` |

#### 2. 动态步态 (Gait)

| 参数类别 | 选项示例 |
|---------|---------|
| 节奏 | `brisk walk`, `slow shuffling gait`, `limping on right leg` |
| 幅度 | `long strides`, `short, quick steps` |
| 姿态 | `swaggering walk` (大摇大摆) / `dragging feet` / `bouncing step` |
| 特殊习惯 | `toes point outward` (外八字) / `knees knock together when walking` |

#### 3. 微表情与肢体语言 (Micro-expressions)

- `nervous tic (touching nose)`
- `scanning the room constantly`
- `avoiding eye contact`

💡 **AIGC 提示词技巧**: 使用动作动词 `walking briskly`, `standing with arms crossed`, `slouching against a wall`，配合 `candid photography` (抓拍) 风格。

---

### 第三维度：衣着与修饰 (Attire & Adornment)

**目标**：通过服装的合身度、风格和磨损情况，反推人物的社会属性和生活习惯。

#### 1. 服装合身度 (Fit & Silhouette)

| 合身类型 | 示例 |
|---------|------|
| 宽松 | `oversized clothing`, `baggy jeans`, `clothes hanging loosely` |
| 紧身 | `tight-fitting shirt`, `skinny jeans`, `clothes straining at the buttons` |
| 不合身 | `ill-fitting suit (sleeves too long)`, `worn-out shoes` |

#### 2. 风格与层级 (Style & Layers)

- **风格**: `business casual`, `streetwear`, `utilitarian/workwear`, `disheveled`
- **层次**: `wearing a hoodie under a denim jacket`, `multiple layers of sweaters`
- **品牌/细节**: `logo-less generic clothing`, `designer label visible`, `military surplus gear`

#### 3. 状态与磨损 (Condition & Wear)

- 衣服：`wrinkled shirt`, `stained collar`, `frayed cuffs`, `polished shoes`, `muddy boots`
- 配饰：`worn-out baseball cap`, `gold chain`, `smartwatch`, `tactical backpack`

💡 **AIGC 提示词技巧**: 描述材质和状态，如 `worn leather jacket`, `crisp white shirt`, `faded denim`。

---

## 📝 描述模板 (结构化输出)

### 【整体印象】
```
[性别] + [大致年龄] + [体型分类] + [身高量级]
```
**例**: 一名 30 岁左右的男性，中胚层运动体型，身高约 180cm，给人压迫感。

### 【骨架细节】
```
肩宽：[描述]
胸腹：[描述]
四肢：[描述]
```
**例**: 肩膀宽阔呈方形，胸部厚实，手臂肌肉线条明显，小腿粗壮。

### 【身姿与动态】
```
站姿：[描述]
手部习惯：[描述]
步态特征：[描述]
```
**例**: 站立时习惯双手插兜，重心后仰。走路步幅大，速度快，略带外八字。

### 【衣着与状态】
```
上装：[款式] + [合身度] + [状态]
下装：[款式] + [合身度] + [状态]
鞋履/配饰：[描述]
整体风格：[总结]
```
**例**: 身穿一件略显紧身的黑色连帽卫衣，袖口有磨损。下穿宽松的灰色运动裤。脚踩一双脏旧的白色运动鞋。整体呈现一种随意的街头风格。

---

## 🚀 AIGC 提示词生成器

### 提示词构建顺序
**主体 + 动作 + 衣着 + 环境 + 镜头语言**

### 示例：嫌疑人身描述

```markdown
**Subject**: Male, 30s, mesomorph athletic build, 180cm tall, broad square shoulders, thick chest, muscular arms.
**Posture**: Standing with weight shifted back, hands deep in pockets, slight slouch, confident demeanor.
**Attire**: Wearing a tight-fitting black hoodie with frayed cuffs, loose gray sweatpants, dirty white sneakers.
**Style**: Streetwear, disheveled, urban criminal suspect style.
**Environment**: Night street, dim streetlight, rain-slicked pavement.
**Camera**: Full body shot, low angle shot (to emphasize height), 35mm lens, realistic texture, 8k.
```

---

## 🎯 一致性提升技巧

### 1. 固定"标志性物品" (Anchor Objects)

在多次生成中，始终保留一个独特的物品：
- "红色的棒球帽"
- "特定的背包"
- "独特的鞋子"
- "特殊配饰"

**效果**: 比单纯依赖脸部更能让观察者感觉是"同一个人"。

### 2. 描述"不完美" (Imperfections)

加入真实感细节：
- `wrinkled shirt` (衣服皱巴巴)
- `loose shoelaces` (鞋带散了)
- `slight belly bulge` (肚子微微突出)
- `faded jeans` (褪色的牛仔裤)

### 3. 使用 ControlNet (OpenPose)

对于身姿的一致性，不要只靠提示词：

1. 找一张符合你描述姿势的照片（或手绘火柴人）
2. 使用 ControlNet OpenPose 插件锁定骨架
3. 无论换脸、换衣服，人物的身高比例、站姿、手脚位置保持绝对一致

### 4. 分层生成策略

**第一步**: 生成全身照
- 确定身材、比例、衣着和姿势
- 此时脸部可以模糊

**第二步**: 使用 Inpaint (重绘)
- 只针对面部区域进行精细化重绘
- 结合"结构化面部提示词"

**效果**: 避免调整脸部细节导致身体比例崩坏。

---

## 📋 快速参考卡片

### 高优先级参数（优先保证一致性）
- ⭐⭐⭐ `mesomorph build`, `ectomorph build` (体型分类)
- ⭐⭐⭐ `185cm tall`, `petite` (身高)
- ⭐⭐⭐ `square shoulders`, `sloping shoulders` (肩部特征)
- ⭐⭐⭐ `hands in pockets`, `arms crossed` (手部习惯)
- ⭐⭐ `tight-fitting`, `oversized` (服装合身度)

### 中优先级参数（可适度调整）
- ⚪ `brisk walk`, `slow shuffling gait` (步态)
- ⚪ `black hoodie`, `gray sweatpants` (具体衣着)
- ⚪ `upright`, `slouched` (脊柱姿态)

### 环境参数（最易变化）
- 🔹 `daylight`, `night`, `studio` (时间/环境)
- 🔹 `rain-slicked pavement`, `urban street` (环境细节)
- 🔹 `35mm lens`, `low angle shot` (镜头语言)

---

## 📚 参考技能

- **`zclaw-consistent-face-prompt`**: 面部特征结构化描述
- **`zclaw-article-to-cartoon-prompt`**: 提示词风格化建议
- **`zclaw-article-recommender`**: 文章推荐序创作

---

## 🎯 适用场景

- 🔍 刑侦模拟画像与嫌疑人描述
- 🎮 游戏角色全身设计
- 🎬 影视角色概念设计
- 🎨 AI 绘画角色一致性维护
- 📖 小说/剧本角色设定
- 🛡️ 安全监控描述分析


## 参考文件

- [`references/prompt-template.md`](references/prompt-templates.md) - 完整提示词模板

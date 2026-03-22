---
name: zclaw-consistent-face-prompt
description: 构建高一致性人脸生成提示词。
---

# - 高一致性人脸生成提示词构建指南

## 技能概述

这是一个专业的 AIGC 人脸生成提示词构建工具，帮助用户通过**结构化特征分解原则**创建高质量、高一致性的人脸生成提示词。将模糊的艺术描述转化为精确、可量化的几何与形态参数，实现跨图像角色一致性和风格可控性。
同时提供中英文两个版本。

## 核心原则

**从模糊到精确：结构化特征分解原则**

将人脸视为一个可量化的几何系统，而非艺术化的整体描述。通过分解为独立参数（性别、年龄、种族、脸型和五官），实现角色一致性和可复制性。

## 基础框架

### 1. 身份层（Identity Layer）
定义角色的基本身份特征：

**性别（Gender）**
- `male` / `female` / `androgynous`

**年龄（Age）**
- `child (3-9)` / `teen (10-19)` / `young adult (20-35)` / `middle-aged (36-55)` / `senior (56+)`

**种族/血统（Ethnicity/Heritage）**
- `East Asian`, `Southeast Asian`, `South Asian`, `Middle Eastern`, `European/Caucasian`, `African/Black`, `Latino/Hispanic`, `mixed-race`

### 2. 脸型层（Face Geometry）
描述面部轮廓结构：

**脸型（Face Shape）**
- `oval` (椭圆形), `round` (圆形), `square` (方形), `heart-shaped` (心形), `diamond-shaped` (菱形), `long/rectangular` (长方形), `triangular` (三角形)

**特征描述**
- `strong jawline` (下颌线分明) / `soft jawline` (柔和下颌线) / `slightly squared` (轻微方形) / `angular chin` (棱角分明的下巴)

**肤色与纹理**
- `fair skin` (白皙肌肤) / `light skin` (浅色肌肤) / `medium skin` (中等肤色) / `olive skin` (橄榄色肌肤) / `tan skin` (晒黑肤色) / `dark skin` (深色肌肤) / `dark brown skin` (深棕色肌肤)
- `smooth skin` (光滑肌肤) / `porous skin` (毛孔可见) / `oily skin` (油性肌肤) / `dewy skin` (水润肌肤)
- `visible pores` (可见毛孔) / `fine texture` (细腻质感)

### 3. 细节层（Distinctive Markings）
识别特征（锚点用于一致性）

**疤痕与斑点**
- `small mole on left cheek` (左脸颊小痣) / `freckles across nose` (鼻翼雀斑) / `scar above eyebrow` (眉上疤痕)

**皱纹（年龄标志）**
- `crow's feet` (眼角皱纹) / `smile lines` (微笑纹) / `forehead lines` (额头纹) / `nasolabial folds` (鼻唇沟)

### 4. 风格层（Style Control）
**背景**
- `solid color background: #HEX` (纯色背景) / `soft gradient background` (柔和渐变背景) / `studio lighting` (影棚灯光) / `natural outdoor` (自然户外)

**光影**
- `softbox lighting` (柔光箱灯光) / `golden hour` (黄金时刻) / `harsh midday sun` (强烈的正午阳光) / `low key lighting` (低调灯光)

分辨率参数
- `4k`, `8k`, `high resolution`

## 五官结构化特征分解（Structured Feature Breakdown）

### 眼部（Eyes）- 特征密度：高
**形状与大小**
- `almond-shaped eyes` (杏仁眼) / `round eyes` (圆眼) / `hooded eyes` (肿眼泡) / `deep-set eyes` (深陷眼)
- `wide eyes` (大眼) / `narrow eyes` (窄眼) / `close-set eyes` (眼距近) / `wide-set eyes` (眼距宽)

**眼睑**
- `single eyelid` (单眼皮) / `double eyelid` (双眼皮) / `monolid` (蒙古睑)
- `thick eyelids` (厚眼皮) / `thin eyelids` (薄眼皮)

**虹膜**
- `hazel eyes` (淡褐色眼) / `green eyes` (绿眼) / `grey eyes` (灰眼) / `blue eyes` (蓝眼) / `brown eyes` (棕眼) / `dark brown eyes` (深棕眼) / `amber eyes` (琥珀色眼)

**眉毛**
- `arched eyebrows` (挑眉) / `straight eyebrows` (平眉) / `thick eyebrows` (浓眉) / `thin eyebrows` (细眉) / `bushy eyebrows` (浓密眉毛)

### 鼻部（Nose）- 特征密度：高
**鼻梁**
- `straight bridge` (直鼻梁) / `high bridge` (高鼻梁) / `low bridge` (低鼻梁) / `Roman nose` (罗马鼻) / `aquiline nose` (鹰钩鼻)

**鼻尖**
- `rounded tip` (圆鼻尖) / `pointed tip` (尖鼻尖) / `upturned nose` (朝天鼻) / `down-turned nose` (下垂鼻尖)

**鼻翼**
- `narrow nostrils` (窄鼻翼) / `flared nostrils` (宽鼻翼) / `small nose` (小鼻子) / `prominent nose` (突出的鼻子) / `button nose` (蒜头鼻)

### 唇部（Mouth/Lips）- 特征密度：中
**唇形**
- `full lips` (丰满唇) / `thin lips` (薄唇) / `medium lips` (中等厚度唇)
- `defined Cupid's bow` (清晰的唇峰) / `soft cupid's bow` (柔和唇峰)
- `heart-shaped lips` (心形唇) / `square lips` (方形唇)

**唇宽与位置**
- `wide mouth` (宽嘴) / `narrow mouth` (窄嘴) / `small mouth` (小嘴)
- `lips to cheekbone` (唇至颧骨) / `lips to nose` (唇至鼻尖)

### 耳部（Ears）- 特征密度：低
- `small ears` (小耳) / `large ears` (大耳) / `button ears` (纽扣耳) / `protruding ears` (招风耳)
- `attached earlobes` (附耳垂) / `detached earlobes` (游离耳垂)

## 使用示例

### 基本结构
```markdown
[性别] [年龄] [种族] [脸型] [肤色] [特征] [眼部特征] [鼻部特征] [唇部特征] [眉毛特征] [背景] [光影] [质量]
```

### 示例 1：东方女性
```markdown
female, young adult (20-35), East Asian, oval face, fair skin, smooth skin, almond-shaped eyes, single eyelid, dark brown eyes, straight nose, full lips, defined Cupid's bow, arched eyebrows, solid color background: #F5DEB3, softbox lighting, 4k
```

### 示例 2：中年男性
```markdown
male, middle-aged (36-55), European/Caucasian, square face, olive skin, visible pores, crow's feet, small mole on left cheek, straight bridge Roman nose, thin lips, thick eyebrows, studio lighting, high resolution
```

## 一致性工作流建议

### 1. 特征清单法
创建角色档案，列出所有特征参数，在多次生成中保持一致性。

### 2. 锚点特征法
确定 2-3 个独特的**锚点特征**（如特定的痣、疤痕或眼型），作为视觉识别标志。

### 3. 参数优先法
始终按照以下顺序组织提示词：
1. 身份层（最稳定）
2. 脸型层（次稳定）
3. 五官层（可调整）
4. 背景光影（最可变）

### 4. 测试与优化
使用 A/B 测试不同的参数组合，记录效果最佳的结构化描述。

## 高级技巧

### 比例控制（通过三庭五眼）
- `face length proportion: 35mm (3 庭)`
- `face width proportion: 25mm (5 眼)`
- `lower face longer than upper`
- `eye间距 = 一只眼睛宽度`

### 年龄标志参数
- `early 20s: smooth skin, no wrinkles`
- `late 40s: nasolabial folds, fine lines around eyes`
- `early 60s: deeper wrinkles, age spots`

### 风格融合
将写实与艺术风格结合：`photorealistic, cinematic portrait, dramatic lighting`

## 注意事项

1. **特征冲突避免**：不要同时使用 `round face` 和 `strong jawline`，它们相互矛盾
2. **参数优先级**：AI 可能无法精确控制所有特征，优先关注高特征密度参数（眼睛、鼻子）
3. **文化敏感性**：描述种族时应保持尊重和准确
4. **过度描述风险**：过多的细节可能降低生成质量，保持适度

## 适用场景

- AI 绘画（Stable Diffusion, Midjourney, DALL-E 3）
- 游戏角色设计
- 故事插图人物创建
- IP 角色一致性维护
- 角色概念艺术

## 参考文件

- [`references/prompt-template.md`](references/prompt-template.md) - 完整提示词模板

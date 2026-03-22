# zclaw-consistent-face-prompt - 使用指南

## 🎯 何时使用此技能

当你需要：

- ✨ **创建角色一致性**：为 IP 角色在不同场景中保持面部特征一致
- 🎨 **精确角色设计**：将模糊的角色描述转化为可执行的技术参数
- 🖼️ **跨图像生成**：在多个生成结果中保持角色识别度
- 🔧 **风格化人脸**：设计具有特定面部特征的角色（如反派、英雄、奇幻生物）
- 📐 **比例控制**：需要精确控制面部比例（三庭五眼、五官位置）

**不建议用于**：纯艺术化、无明确特征要求的抽象人脸创作。

## 🧠 核心理念：结构特征分解

传统提示词描述方式通常模糊且不可控：

> "一个美丽的东方女性，大眼睛，精致的五官"

这种描述无法保证**一致性**和**可复制性**。

本技能采用**结构特征分解原则**：

将人脸视为一个由独立参数组成的几何系统，每个参数都可以量化和调整：

### 分解思维

```
模糊描述 → 结构化的参数集合

美丽的东方女性 →
  - 性别：female
  - 年龄：young adult (20-35)
  - 种族：East Asian
  - 脸型：oval
  - 肤色：fair skin, smooth skin
  - 眼部：almond-shaped, single eyelid, dark brown
  - 鼻部：straight bridge, rounded tip
  - 唇部：full lips, defined Cupid's bow
  - 眉毛：arched
```

## 📋 快速参考指南

### 核心参数速查表

| 参数类别 | 关键参数 | 示例值 |
|---------|---------|--------|
| **身份** | 性别 | `male`, `female`, `androgynous` |
| | 年龄 | `child`, `teen`, `young adult`, `middle-aged`, `senior` |
| | 种族 | `East Asian`, `European`, `African` 等 |
| **脸型** | 轮廓 | `oval`, `round`, `square`, `heart` |
| | 特征 | `strong jawline`, `soft jawline` |
| | 肤色 | `fair`, `olive`, `dark brown` |
| **眼部** | 形状 | `almond`, `round`, `hooded` |
| | 眼睑 | `double eyelid`, `monolid` |
| | 虹膜 | `hazel`, `green`, `brown`, `grey` |
| **鼻部** | 鼻梁 | `straight`, `high bridge`, `Roman` |
| | 鼻尖 | `rounded`, `pointed`, `upturned` |
| **唇部** | 唇形 | `full`, `thin`, `heart-shaped` |
| **标注** | 识别点 | `small mole on cheek`, `scar above eyebrow` |

### 提示词构建模板

```markdown
[性别] [年龄] [种族] [脸型] [肤色] [特征标记]
[眼部描述] [鼻部描述] [唇部描述] [眉毛描述]
[背景描述] [光影描述] [质量/分辨率]
```

## 📚 完整使用流程

### 第 1 步：确定角色身份（基础）

**问题清单**：
- 性别是什么？
- 年龄段？
- 种族背景？

**输出**：
```
female, young adult, East Asian
```

### 第 2 步：分解面部特征（核心）

**系统提问**：
1. 脸型是什么类型？（从：oval, round, square, heart, diamond）
2. 肤色和质感？
3. 眼部特征？（形状、眼睑、虹膜、眼睛位置）
4. 鼻部特征？（鼻梁、鼻尖、鼻翼）
5. 唇部特征？（厚度、形状、唇峰）
6. 眉毛特征？
7. 是否有独特的**锚点特征**？（痣、疤痕、皱纹等）

**输出**：
```
oval face, fair skin, smooth skin,
almond-shaped eyes, single eyelid, dark brown eyes,
straight bridge nose, rounded tip,
full lips, defined Cupid's bow,
arched eyebrows,
small mole on left cheek, fine crow's feet
```

### 第 3 步：添加语境和风格（可选）

1. 背景设定是什么？
2. 光影偏好？
3. 分辨率要求？

**输出**：
```
studio lighting, softbox, 4k, high resolution
```

## 🎨 实用示例

### 示例 A：从模糊到精确

**模糊描述**：
```
"一个看起来 30 岁左右的女性，亚洲人特征，温柔的微笑"
```

**结构化描述**：
```
female, young adult (20-35), East Asian,
oval face, fair skin, smooth
warm eyes, double eyelid, dark brown eyes,
soft smile lines, straight bridge nose,
full lips, soft Cupid's bow,
arched eyebrows,
studio portrait, softbox lighting, 4k
```

### 示例 B：角色一致性

**角色名称：陈思思**
```
female, young adult (20-35), East Asian,
oval face, fair skin,
almond-shaped eyes, single eyelid, dark brown eyes,
straight nose, rounded tip,
full lips, small mole on left cheek,
arched eyebrows,
studio lighting, cinematic lighting, 8k
```

**关键锚点特征**：`small mole on left cheek`, `single eyelid`

每次生成时保持这两个参数不变。

## 💡 高级技巧

### 1. 三庭五眼比例控制

使用比例参数控制面部和谐度：
```
face length proportion: 35mm (3 庭)
face width proportion: 25mm (5 眼)
eye间距 = 一只眼睛宽度
```

### 2. 年龄标志描述

根据年龄调整细节描述：
- **20 多岁**：`smooth skin`, `no wrinkles`
- **40 多岁**：`nasolabial folds`, `crow's feet`
- **60 岁+**：`deeper wrinkles`, `age spots`, `visible skin texture`

### 3. 特征优先级

AI 对不同特征的敏感度不同：
1. **高敏感度**：眼睛、鼻子形状
2. **中敏感度**：脸型、唇形
3. **低敏感度**：耳部、细微特征

优先保证高敏感度特征的一致性。

## 🛠️ 与主流工具的兼容性

### Stable Diffusion
```python
prompt = "female, young adult, East Asian, oval face, fair skin, smooth skin, almond-shaped eyes, double eyelid, dark brown eyes, straight bridge nose, full lips, defined Cupid's bow, arched eyebrows, studio lighting, 4k"
negative_prompt = "oversaturated, distorted face, asymmetric eyes, extra limbs"
```

### Midjourney
```
/female young adult East Asian oval face fair skin smooth skin almond-shaped eyes single eyelid dark brown eyes straight bridge nose full lips defined Cupid's bow arched eyebrows small mole on cheek studio lighting cinematic --ar 3:4 --stylize 250 --v 6.0
```

### DALL-E 3
```text
一个 20-35 岁的年轻东亚女性，椭圆形脸型，白皙光滑肌肤，杏仁眼，单眼皮，深棕色眼睛，直鼻梁圆鼻尖，丰满嘴唇清晰唇峰，上挑眉，左脸颊小痣，影棚灯光，电影感构图，4K 分辨率
```

## ⚠️ 常见问题

### Q: 为什么我的角色不一致？
A: 确保至少 2-3 个**锚点特征**在所有生成中保持不变。建议：眼睛类型（almond/round）、独特标记（痣/疤痕）、脸型（oval/round/square）。

### Q: 是否所有参数都需要？
A: 不需要。建议至少包含：性别、年龄、种族、脸型、眼睛特征、鼻子特征。其他参数可选。

### Q: 如何处理种族敏感问题？
A: 使用通用术语如 `mixed-race` 或具体种族。避免刻板印象和贬低性描述。

### Q: 可以修改特征吗？
A: 可以，但修改高敏感度特征（眼睛、鼻子）会显著影响角色识别度。

# 提示词构建参考模板

本文件提供了完整的面部特征参数列表和构建提示词的详细指南。

---

## 📋 参数参考库

### 身份层参数

| 参数类别 | 选项列表 | 说明 |
|---------|---------|------|
| 性别 | `male`, `female`, `androgynous` | 基础性别标识 |
| 年龄 | `child (3-9)`, `teen (10-19)`, `young adult (20-35)`, `middle-aged (36-55)`, `senior (56+)` | 年龄段划分 |
| 种族 | `East Asian`, `Southeast Asian`, `South Asian`, `Middle Eastern`, `European/Caucasian`, `African/Black`, `Latino/Hispanic`, `mixed-race` | 种族/血统背景 |

### 脸型层参数

| 参数类别 | 选项列表 | 说明 |
|---------|---------|------|
| 脸型 | `oval`, `round`, `square`, `heart-shaped`, `diamond-shaped`, `long/rectangular`, `triangular` | 面部轮廓形状 |
| 下颌特征 | `strong jawline`, `soft jawline`, `slightly squared`, `angular chin` | 下颌线特征 |
| 肤色 | `fair skin`, `light skin`, `medium skin`, `olive skin`, `tan skin`, `dark skin`, `dark brown skin` | 肤色深浅 |
| 皮肤质感 | `smooth skin`, `porous skin`, `oily skin`, `dewy skin`, `visible pores`, `fine texture` | 皮肤表面质感 |

### 细节层参数

| 参数类别 | 选项列表 | 说明 |
|---------|---------|------|
| 痣/斑点 | `small mole on left cheek`, `small mole on right cheek`, `small mole on chin`, `freckles across nose`, `freckles on cheeks` | 识别性标记 |
| 疤痕 | `scar above eyebrow`, `scar on chin`, `small scar on temple` | 疤痕特征 |
| 皱纹 | `crow's feet` (眼角), `smile lines` (微笑纹), `forehead lines` (额头), `nasolabial folds` (鼻唇沟), `deep forehead wrinkles`, `fine lines around eyes` | 年龄标志 |

### 眼部特征参数

| 参数类别 | 选项列表 | 说明 |
|---------|---------|------|
| 形状 | `almond-shaped eyes`, `round eyes`, `hooded eyes`, `deep-set eyes` | 眼部基本形状 |
| 大小 | `wide eyes`, `narrow eyes`, `large eyes`, `small eyes` | 眼睛大小 |
| 间距 | `close-set eyes`, `wide-set eyes` | 眼间距 |
| 眼睑类型 | `single eyelid`, `double eyelid`, `monolid`, `thick eyelids`, `thin eyelids` | 眼皮类型 |
| 虹膜颜色 | `brown eyes`, `dark brown eyes`, `hazel eyes`, `green eyes`, `grey eyes`, `blue eyes`, `amber eyes` | 虹膜颜色 |

### 鼻部特征参数

| 参数类别 | 选项列表 | 说明 |
|---------|---------|------|
| 鼻梁 | `straight bridge`, `high bridge`, `low bridge`, `Roman nose`, `aquiline nose`, `slightly curved bridge` | 鼻梁形状 |
| 鼻尖 | `rounded tip`, `pointed tip`, `upturned nose`, `down-turned nose`, `slightly pointed` | 鼻尖形状 |
| 鼻翼 | `narrow nostrils`, `flared nostrils`, `small nose`, `prominent nose`, `button nose`, `narrow nose` | 鼻翼大小 |

### 唇部特征参数

| 参数类别 | 选项列表 | 说明 |
|---------|---------|------|
| 厚度 | `full lips`, `thin lips`, `medium lips`, `plump lips` | 嘴唇厚度 |
| 形状 | `heart-shaped lips`, `square lips`, `soft Cupid's bow`, `defined Cupid's bow`, `rounded Cupid's bow` | 唇形特征 |
| 宽度 | `wide mouth`, `narrow mouth`, `small mouth` | 嘴巴宽度 |
| 比例参考 | `lips to cheekbone`, `lips to nose`, `lips to chin` | 位置参考 |

### 眉毛特征参数

| 参数类别 | 选项列表 | 说明 |
|---------|---------|------|
| 形状 | `arched eyebrows`, `straight eyebrows`, `flat eyebrows`, `curved eyebrows` | 眉形 |
| 密度 | `thick eyebrows`, `thin eyebrows`, `bushy eyebrows`, `natural eyebrows` | 眉毛密度 |
| 位置 | `high eyebrows`, `low eyebrows`, `relaxed eyebrows` | 眉毛位置 |

### 耳部特征参数

| 参数类别 | 选项列表 | 说明 |
|---------|---------|------|
| 大小 | `small ears`, `large ears`, `button ears`, `protruding ears` | 耳朵大小 |
| 耳垂类型 | `attached earlobes`, `detached earlobes`, `hanging earlobes` | 耳垂形态 |

### 背景与光影参数

| 参数类别 | 选项列表 | 说明 |
|---------|---------|------|
| 背景类型 | `solid color background: #HEX`, `soft gradient background`, `neutral background`, `studio backdrop` | 背景类型 |
| 光影类型 | `softbox lighting`, `golden hour`, `harsh midday sun`, `low key lighting`, `high key lighting`, `natural outdoor`, `ring light`, `rembrandt lighting` | 光影效果 |
| 质量参数 | `4k`, `8k`, `high resolution`, `ultra detailed`, `photorealistic` | 质量标准 |

---

## 🔧 构建示例：从模糊到结构

### 场景 A：年轻东亚女性

**原始模糊描述**：
```
"一个 20 多岁的东亚女性，看起来很温柔，大眼睛，有东方特色"
```

**结构化解析**：

| 描述元素 | 对应参数 | 参数值 |
|---------|---------|--------|
| 20 多岁 | 年龄 | `young adult (20-35)` |
| 东亚 | 种族 | `East Asian` |
| 温柔 | 表情特征 | `soft expression`, `smile lines` |
| 大眼睛 | 眼睛大小 | `relatively wide eyes` |
| 东方特色 | 整体特征 | `almond-shaped eyes`, `single eyelid` |

**结构化提示词**：
```markdown
female, young adult (20-35), East Asian, 
oval face, fair skin, smooth skin, 
almond-shaped eyes, single eyelid, dark brown eyes, 
straight bridge nose, rounded tip, 
medium lips, defined Cupid's bow, 
soft expression, gentle smile lines, 
relaxed eyebrows, 
studio portrait, softbox lighting, golden hour, 
4k, high resolution
```

### 场景 B：中年男性

**原始模糊描述**：
```
"一个看起来可靠的中年白人男性，有胡茬，眼神坚定"
```

**结构化解析**：

| 描述元素 | 对应参数 | 参数值 |
|---------|---------|--------|
| 中年 | 年龄 | `middle-aged (36-55)` |
| 白人 | 种族 | `European/Caucasian` |
| 可靠的 | 表情特征 | `confident expression` |
| 有胡茬 | 细节特征 | `light stubble`, `five o'clock shadow` |
| 眼神坚定 | 眼部特征 | `sharp gaze`, `slightly furrowed brow` |

**结构化提示词**：
```markdown
male, middle-aged (36-55), European/Caucasian, 
square face, olive skin, visible pores, 
deep-set eyes, double eyelid, brown eyes, 
sharp gaze, slightly furrowed brow, 
straight bridge nose, prominent nose, 
thin lips, no smile lines, 
heavy stubble, light beard, 
thick eyebrows, 
studio lighting, low key lighting, 
high resolution
```

### 场景 C：老年女性

**原始模糊描述**：
```
"一个看起来智慧的老年亚洲女性，慈祥的笑容"
```

**结构化解析**：

| 描述元素 | 对应参数 | 参数值 |
|---------|---------|--------|
| 老年 | 年龄 | `senior (56+)` |
| 亚洲 | 种族 | `East Asian` |
| 智慧的 | 表情特征 | `wise expression`, `kind eyes` |
| 慈祥的笑容 | 表情特征 | `warm smile`, `crow's feet`, `smile lines` |

**结构化提示词**：
```markdown
female, senior (56+), East Asian, 
oval face, medium skin, visible texture, 
almond-shaped eyes, single eyelid, deep brown eyes, 
straight bridge nose, slightly flattened tip, 
thin lips, deep smile lines, 
wisdom wrinkles, crow's feet, nasolabial folds, 
warm smile, kind expression, 
relaxed eyebrows, 
natural outdoor lighting, golden hour, 
4k, ultra detailed
```

---

## 🔄 一致性工作流（3 步法）

### 第 1 步：创建角色档案

为每个角色创建基础档案，包含**不可变量**：

```yaml
角色名：陈思思
不可变量（必须保持一致）:
  - 性别：female
  - 年龄：young adult (20-35)
  - 种族：East Asian
  - 脸型：oval face
  - 肤色：fair skin
  - 眼部形状：almond-shaped eyes
  - 眼睑类型：single eyelid
  - 虹膜颜色：dark brown eyes
  - 独特标记：small mole on left cheek

可变量（可根据场景调整）:
  - 服装
  - 背景
  - 光影
  - 表情
```

### 第 2 步：识别锚点特征

每个角色需要 2-3 个**锚点特征**作为识别标志：

| 锚点类型 | 示例 | 重要性 |
|---------|------|--------|
| 眼部形状 | `almond-shaped eyes` | ⭐⭐⭐ 高 |
| 独特标记 | `small mole on left cheek` | ⭐⭐⭐ 高 |
| 脸型 | `oval face` | ⭐⭐ 中 |
| 眼睑类型 | `single eyelid` | ⭐⭐ 中 |
| 眉毛形状 | `arched eyebrows` | ⭐ 低 |

**选择锚点特征时应注意**：
- 高特征密度参数（眼睛、鼻子）更可靠
- 独特标记（痣、疤痕、皱纹）易于识别
- 脸型是稳定的整体特征

### 第 3 步：构建与测试

**构建流程**：
1. 复制角色档案基础参数
2. 保留所有不可变量
3. 添加场景相关参数
4. 测试生成效果

**测试流程**：
```bash
# 第一轮：基本参数测试
生成 4 张，观察锚点特征是否一致

# 第二轮：调整光影和背景
固定基础参数，尝试不同光影

# 第三轮：微调表情和角度
保持基础参数，测试不同表情
```

---

## 📝 提示词速写模板

### 模板 A：标准角色

```markdown
[性别], [年龄] ([年龄范围]), [种族], 
[脸型] 脸，[肤色] 肌肤，[皮肤质感]
[眼部形状] 眼，[眼睑]，[虹膜颜色] 眼，
[鼻梁] 鼻梁鼻，[鼻尖] 鼻尖，
[唇形] 唇，[唇峰特征]，
[眉毛] 眉毛，
[独特标记]
[背景]，[光影]，[质量]
```

### 模板 B：快速构建

```markdown
[性别] [年龄] [种族] [脸型] [肤色]  [眼]  [鼻]  [唇]  [眉]  [光影]，[质量]
```

示例：
```markdown
female young adult East Asian oval face fair skin almond eyes single eyelid dark brown straight bridge nose full lips arched eyebrows softbox lighting 4k
```

### 模板 C：锚点优先

```markdown
[锚点特征 1], [锚点特征 2], 
[基础身份], [脸型], [肤色],
[其他五官],
[光影], [质量]
```

示例：
```markdown
almond-shaped eyes, small mole on left cheek,
female young adult East Asian oval face fair skin,
single eyelid dark brown eyes straight bridge nose full lips,
studio lighting 4k
```

---

## 🎨 风格融合建议

### 写实风格
```markdown
photorealistic, cinematic portrait, natural lighting, 
detailed skin texture, realistic eyes, 
studio quality
```

### 艺术风格
```markdown
stylized, artistic portrait, painted style, 
soft edges, impressionistic, 
concept art, digital painting
```

### 复古风格
```markdown
vintage portrait, film grain, 
sepia tones, retro aesthetic, 
1950s photography style
```

### 幻想风格
```markdown
fantasy portrait, ethereal lighting, 
magical glow, otherworldly, 
concept design, fantasy art
```

---

## ⚡ 快速参考卡片

### 高特征密度参数（优先保证一致性）
- ✅ `almond-shaped eyes` / `round eyes` / `hooded eyes`
- ✅ `single eyelid` / `double eyelid`
- ✅ `straight bridge nose` / `Roman nose` / `aquiline nose`
- ✅ `full lips` / `thin lips`
- ✅ `small mole on [位置]` / `scar on [位置]`

### 中特征密度参数（可适度调整）
- ⚪ `oval face` / `round face` / `square face` / `heart-shaped`
- ⚪ `fair skin` / `olive skin` / `dark brown skin`
- ⚪ `arched eyebrows` / `straight eyebrows`

### 低特征密度参数（最易变化）
- 🔹 `attached earlobes` / `detached earlobes`
- 🔹 `bow-shaped lips` / `heart-shaped lips`
- 🔹 `slight smile lines` vs `deep nasolabial folds`

---

**版本**: 1.0  
**维护者**: OpenClaw Community

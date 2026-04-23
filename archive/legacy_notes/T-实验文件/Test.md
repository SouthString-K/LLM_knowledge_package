---
banner: "[[wallhaven-45vv71.webp]]"
pixel-banner-flag-color: checkers
TQ_explain: 
banner-x: 27
banner-y: 20
---
```dataviewjs
// Update this object
const trackerData = {
    entries: [],
    separateMonths: true,
    heatmapTitle: "This is the title for your heatmap",
    heatmapSubtitle: "This is the subtitle for your heatmap. You can use it as a description.",
}

// Path to the folder with notes
const PATH_TO_YOUR_FOLDER = "daily notes preview/notes";
// Name of the parameter you want to see on this heatmap
const PARAMETER_NAME = 'steps';

// You need dataviewjs plugin to get information from your pages
for(let page of dv.pages(`"${PATH_TO_YOUR_FOLDER}"`).where((p) => p[PARAMETER_NAME])){
    trackerData.entries.push({
        date: page.file.name,
        intensity: page[PARAMETER_NAME],
        content: await dv.span(`[](${page.file.name})`)
    });
}

renderHeatmapTracker(this.container, trackerData);
```
# 一级标题

## 二级标题

### 三级标题

#### 四级标题

##### 五级标题

###### 六级标题

| 1   | 2   |     |
| --- | --- | --- |
| 5   | 6   |     |
| 3   | 4   |     |
这是一个测试文件
这是一个测试文件


```widgets
type: quote
quote: Lorem ipsum dolor sit amet
author: Lorem Ipsum
```


```widgets
type: clock
format: "12hr" | "24hr"
```



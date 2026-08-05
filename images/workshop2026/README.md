# Workshop 2026 Gallery Images

将活动期间的图片放在这个目录中，然后更新 `workshop/2026/gallery.md` 文件来添加图片到画廊。

## 从摄影网站获取图片

如果你想从 `https://live.photoplus.cn/live/pc/82807122/#/live` 获取图片，请按以下步骤操作：

### 方法1：手动下载（推荐）
1. 访问该摄影网站
2. 选择想要的照片
3. 点击下载按钮保存到本地
4. 将下载的图片复制到 `images/workshop2026/` 目录
5. 按照下面的格式添加到 `gallery.md`

### 方法2：批量下载脚本
如果你有该网站的直接图片链接，可以使用以下脚本批量下载：

```bash
# 创建下载脚本
cat > download_gallery_images.sh << 'EOF'
#!/bin/bash
# 从摄影网站批量下载图片的脚本
# 将实际的图片URL替换下面的示例URL

# 示例URL数组 - 请替换为实际的图片URL
urls=(
  "https://example.com/photo1.jpg"
  "https://example.com/photo2.jpg"
  "https://example.com/photo3.jpg"
)

# 下载图片
for i in "${!urls[@]}"; do
  url="${urls[$i]}"
  filename="images/workshop2026/photo$((i+1)).jpg"
  echo "Downloading $url to $filename..."
  curl -o "$filename" "$url"
done

echo "Download complete!"
EOF

chmod +x download_gallery_images.sh
./download_gallery_images.sh
```

## 添加图片到Gallery的步骤

### 步骤1：上传图片
将图片文件放到这个目录 (`images/workshop2026/`)

### 步骤2：更新gallery.md
在 `workshop/2026/gallery.md` 中的 `<div class="gallery-grid">` 部分添加图片项

### 步骤3：测试预览
访问 https://pebble-biofusion.github.io/workshop/2026/gallery/ 查看效果

## 图片格式模板

复制以下模板并替换图片文件名和信息：

```html
<div class="gallery-item">
  <div class="gallery-image-wrapper">
    <img src="{{ site.baseurl }}/images/workshop2026/your-photo.jpg" 
         alt="Workshop photo" 
         class="gallery-image"
         data-full="{{ site.baseurl }}/images/workshop2026/your-photo.jpg"
         data-title="Photo Title"
         data-description="Detailed photo description">
    <div class="gallery-overlay">
      <div class="gallery-overlay-content">
        <button class="view-btn" title="View Full Size">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            <line x1="11" y1="8" x2="11" y2="14"></line>
            <line x1="8" y1="11" x2="14" y2="11"></line>
          </svg>
        </button>
        <button class="download-btn" title="Download Image">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
            <polyline points="7 10 12 15 17 10"></polyline>
            <line x1="12" y1="15" x2="12" y2="3"></line>
          </svg>
        </button>
        <button class="share-btn" title="Share Image">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="18" cy="5" r="3"></circle>
            <circle cx="6" cy="12" r="3"></circle>
            <circle cx="18" cy="19" r="3"></circle>
            <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line>
            <line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line>
          </svg>
        </button>
      </div>
    </div>
  </div>
</div>
```

## 支持的图片格式

- **JPG/JPEG**: 推荐，文件大小适中
- **PNG**: 适合需要透明背景的图片  
- **WebP**: 现代格式，压缩效果好

## 推荐的图片规格

- **宽度**: 至少1200px（确保清晰度）
- **高宽比**: 4:3 或 16:9 效果最佳
- **文件大小**: 建议每张图片小于2MB
- **质量**: 高质量，避免过度压缩

## Gallery功能特性

✨ **现代网格布局** - 响应式设计，自动适配各种屏幕  
🖼️ **点击查看大图** - 专业的Lightbox效果  
⬇️ **下载功能** - 一键下载高清图片  
🔗 **分享功能** - 支持原生分享或复制链接  
🎨 **现代简约风格** - 注重图片本身，界面简洁  
📱 **移动端友好** - 在各种设备上完美显示

## 注意事项

1. **文件命名**: 使用有意义的文件名，如 `workshop-opening.jpg` 而不是 `photo1.jpg`
2. **版权信息**: 确保有权限使用这些照片
3. **图片优化**: 压缩大图片以提高加载速度
4. **描述信息**: 为每张照片添加有意义的标题和描述

## 快速开始示例

如果你有5张照片要添加，可以这样组织：

```html
<div class="gallery-grid">
  
  <!-- Opening Ceremony -->
  <div class="gallery-item">
    <div class="gallery-image-wrapper">
      <img src="{{ site.baseurl }}/images/workshop2026/opening-ceremony.jpg" 
           alt="Workshop Opening Ceremony" 
           class="gallery-image"
           data-full="{{ site.baseurl }}/images/workshop2026/opening-ceremony.jpg"
           data-title="Workshop Opening Ceremony"
           data-description="Group photo from the opening ceremony of Pebble BioFusion Workshop 2026">
      <!-- overlay buttons -->
    </div>
  </div>

  <!-- More photos... -->
  
</div>
```

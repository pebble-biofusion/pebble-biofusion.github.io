# Workshop 2026 Gallery Images

将活动期间的图片放在这个目录中，然后更新 `workshop/2026/gallery.md` 文件来添加图片到画廊。

## 添加图片的步骤：

1. **上传图片**：将图片文件放到这个目录
2. **更新gallery.md**：在 `workshop/2026/gallery.md` 中的 `<div class="gallery-grid">` 部分添加图片项

## 图片格式示例：

```html
<div class="gallery-item">
  <a href="{{ site.baseurl }}/images/workshop2026/your-photo.jpg" class="gallery-link" target="_blank">
    <img src="{{ site.baseurl }}/images/workshop2026/your-photo.jpg" alt="Photo description">
  </a>
  <div class="gallery-caption">Your photo description here</div>
</div>
```

## 支持的图片格式：

- JPG/JPEG
- PNG  
- WebP

## 建议的图片尺寸：

- 宽度：至少800px
- 高宽比：4:3或16:9效果最佳
- 文件大小：建议每张图片小于2MB

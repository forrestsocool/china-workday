# China Workday

适用于中国节假日的工作日插件。

## 安装

方法1：下载并复制`custom_components/china_workday`文件夹到HomeAssistant根目录下的`custom_components`文件夹即可完成安装

方法2：已经安装了HACS，可以点击按钮快速安装 [![通过HACS添加集成](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=forrestsocool&repository=china-workday&category=integration)

## 配置

配置 > 设备与服务 >  集成 >  添加集成 > 搜索`china workday`

或者点击: [![添加集成](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start?domain=china_workday)

## 调试
在`configuration.yaml`中加入以下配置来打开调试日志。

```yaml
logger:
  default: warn
  logs:
    custom_components.china_workday: debug
```


## 数据来源
- https://github.com/NateScarlet/holiday-cn

## 版本

### 0.0.4 (2026-07-17)

- 将非法的集成 domain `china-workday` 迁移为 `china_workday`，使 Home Assistant 能加载本地品牌图标
- 保留原实体 unique ID，升级后 `binary_sensor.is_workday` 不会重复创建

### 0.0.3 (2026-07-17)

- 修复 Home Assistant 2026.7 对非法实体 ID 的兼容性警告
- 添加透明背景的本地品牌图标和 Logo

import argostranslate.package
import argostranslate.translate
from_code = "en"
to_code = "es"
# 加载已安装的语言包
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)
# 获取翻译模型（例如，从英语到西班牙语）
argostranslate.package.install_from_path(package_to_install.download())

# 执行翻译
translatedText = argostranslate.translate.translate(
    "Hello World", from_code, to_code)
print(translatedText)
# '¡Hola Mundo!'

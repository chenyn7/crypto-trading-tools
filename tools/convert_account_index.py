#!/usr/bin/env python3
"""
Lighter Account Index 进制转换工具 转换工具

支持：
- 十进制 ↔ 十六进制
- 十六进制 ↔ 十进制
- 自动识别输入格式
"""

import sys


def auto_detect_and_convert(value: str) -> None:
    """自动识别输入格式并转换"""
    value = value.strip()

    print("=" * 70)
    print("🔄 Lighter Account Index 进制转换工具")
    print("=" * 70)
    print()

    # 检测输入格式
    if value.startswith('0x') or value.startswith('0X'):
        # 十六进制输入
        hex_value = value
        try:
            dec_value = int(hex_value, 16)
            print(f"📥 输入 (十六进制): {hex_value}")
            print()
            print(f"📤 输出 (十进制):   {dec_value}")
            print()
            print("✅ 转换完成！")
        except ValueError as e:
            print(f"❌ 错误：无效的十六进制值 - {e}")

    elif value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
        # 十进制输入
        dec_value = int(value)
        hex_value = hex(dec_value)

        print(f"📥 输入 (十进制):   {dec_value}")
        print()
        print(f"📤 输出 (十六进制): {hex_value}")
        print()
        print("✅ 转换完成！")

    else:
        # 尝试作为十六进制（不带0x前缀）
        try:
            dec_value = int(value, 16)
            hex_value = f"0x{value}"

            print(f"📥 输入 (十六进制): {hex_value}")
            print()
            print(f"📤 输出 (十进制):   {dec_value}")
            print()
            print("✅ 转换完成！")
        except ValueError:
            print(f"❌ 错误：无法识别的输入格式")
            print(f"   输入值: {value}")
            print()
            print("💡 支持的格式：")
            print("   - 十进制: 123456")
            print("   - 十六进制: 0x1e240 或 1e240")

    print("=" * 70)
    print()


def interactive_mode():
    """交互式模式"""
    print("=" * 70)
    print("🔄 Lighter Account Index 进制转换工具 (交互模式)")
    print("=" * 70)
    print()
    print("💡 使用说明：")
    print("   - 输入十进制数字（如：123456）")
    print("   - 输入十六进制数字（如：0x1e240 或 1e240）")
    print("   - 输入 'q' 或 'quit' 退出")
    print("=" * 70)
    print()

    while True:
        try:
            value = input("请输入 account_index: ").strip()

            if value.lower() in ['q', 'quit', 'exit']:
                print()
                print("👋 再见！")
                break

            if not value:
                continue

            print()
            auto_detect_and_convert(value)

        except KeyboardInterrupt:
            print()
            print()
            print("👋 再见！")
            break
        except EOFError:
            break


def batch_mode(values: list):
    """批量转换模式"""
    print("=" * 70)
    print("🔄 Lighter Account Index 进制转换工具 (批量模式)")
    print("=" * 70)
    print()

    for i, value in enumerate(values, 1):
        print(f"【{i}/{len(values)}】")
        auto_detect_and_convert(value)
        if i < len(values):
            print()


def show_examples():
    """显示示例"""
    print("=" * 70)
    print("📚 使用示例")
    print("=" * 70)
    print()

    print("1️⃣ 十进制 → 十六进制")
    print("   输入: 123456")
    print("   输出: 0x1e240")
    print()

    print("2️⃣ 十六进制 → 十进制")
    print("   输入: 0x1e240")
    print("   输出: 123456")
    print()

    print("3️⃣ 十六进制（不带0x） → 十进制")
    print("   输入: 1e240")
    print("   输出: 123456")
    print()

    print("4️⃣ 命令行使用")
    print("   单个转换: python convert_account_index.py 123456")
    print("   批量转换: python convert_account_index.py 123456 0x1e240 abc123")
    print("   交互模式: python convert_account_index.py")
    print()

    print("5️⃣ 实际案例")
    print("   # Lighter API 通常使用十进制")
    print("   输入: 0")
    print("   输出: 0x0")
    print()
    print("   # 前端可能显示十六进制")
    print("   输入: 0x7b")
    print("   输出: 123")
    print()

    print("=" * 70)


def show_help():
    """显示帮助信息"""
    print("=" * 70)
    print("🔄 Lighter Account Index 进制转换工具")
    print("=" * 70)
    print()
    print("用法:")
    print("  python convert_account_index.py [VALUES...]")
    print("  python convert_account_index.py --help")
    print("  python convert_account_index.py --examples")
    print()
    print("参数:")
    print("  VALUES     要转换的值（支持多个）")
    print("  --help     显示此帮助信息")
    print("  --examples 显示使用示例")
    print()
    print("模式:")
    print("  无参数     启动交互式模式")
    print("  单个值     转换单个值")
    print("  多个值     批量转换")
    print()
    print("支持的格式:")
    print("  十进制:   123456, -123")
    print("  十六进制: 0x1e240, 0X1E240, 1e240, 1E240")
    print()
    print("=" * 70)


def main():
    """主函数"""
    args = sys.argv[1:]

    # 无参数：交互模式
    if not args:
        interactive_mode()
        return

    # 帮助信息
    if args[0] in ['--help', '-h', 'help']:
        show_help()
        return

    # 示例
    if args[0] in ['--examples', '-e', 'examples']:
        show_examples()
        return

    # 单个值或批量转换
    if len(args) == 1:
        auto_detect_and_convert(args[0])
    else:
        batch_mode(args)


if __name__ == "__main__":
    main()

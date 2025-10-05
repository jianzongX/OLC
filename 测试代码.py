import requests
from bs4 import BeautifulSoup

def fetch_content_between_markers():
    url = "https://jianzongx.github.io/OLC/"
    
    # 设置请求头，模拟浏览器访问
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    
    try:
        # 发送GET请求
        print(f"正在获取页面内容: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        
        # 检查请求是否成功
        response.raise_for_status()
        
        # 获取页面文本内容
        page_text = response.text
        
        # 定义开始和结束标记
        start_marker = "t-t-t"
        end_marker = "f-f-f"
        
        # 查找开始标记的位置
        start_index = page_text.find(start_marker)
        if start_index == -1:
            print(f"未找到开始标记: {start_marker}")
            return
        
        # 计算开始标记之后的位置（跳过开始标记本身）
        start_index += len(start_marker)
        
        # 查找结束标记的位置
        end_index = page_text.find(end_marker, start_index)
        if end_index == -1:
            print(f"未找到结束标记: {end_marker}")
            return
        
        # 提取两个标记之间的内容
        content_between = page_text[start_index:end_index].strip()
        
        # 如果内容包含HTML标签，尝试提取纯文本
        if '<' in content_between and '>' in content_between:
            soup = BeautifulSoup(content_between, 'html.parser')
            content_between = soup.get_text(separator='\n', strip=True)
        
        # 显示结果
        if content_between:
            print("\n成功提取标记之间的内容:\n")
            print(content_between)
        else:
            print("\n标记之间没有找到内容")
            
    except requests.exceptions.RequestException as e:
        print(f"请求发生错误: {e}")
    except Exception as e:
        print(f"处理页面时发生错误: {e}")

if __name__ == "__main__":
    fetch_content_between_markers()
    

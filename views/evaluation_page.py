import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def show_evaluation_page(df):
    st.title("🎯 Đánh giá Mô hình & Hiệu suất")
    
    st.markdown("""
    Trang này đánh giá hiệu suất của các thuật toán **Lọc Dựa trên Luật (Rule-Based Filtering)** và **Bài toán Thỏa mãn Ràng buộc (CSP)**.
    """)
    
    # Mock evaluation metrics for demonstration
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📌 Chỉ số Đánh giá")
    col1, col2 = st.columns(2)
    col1.metric("Tỷ lệ Thỏa mãn Ràng buộc", "94.5%", "+2.1%")
    col2.metric("Điểm Dinh dưỡng Trung bình", "8.7 / 10", "+0.4")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📉 Trực quan hóa")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("**Mức độ Thỏa mãn Ràng buộc theo Dinh dưỡng**")
        fig, ax = plt.subplots(figsize=(6, 5))
        categories = ['Calo', 'Protein', 'Đường', 'Natri', 'Chất béo']
        satisfaction = [95, 98, 92, 89, 94]
        ax.bar(categories, satisfaction, color=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
        ax.set_ylim(0, 100)
        ax.set_ylabel("Tỷ lệ Thỏa mãn (%)")
        st.pyplot(fig)
        
    with c2:
        st.markdown("**Phân bố Dinh dưỡng (Thực đơn Mẫu vs Mục tiêu)**")
        fig2, ax2 = plt.subplots(figsize=(6, 5))
        
        # Radar chart
        labels=np.array(['Calo', 'Protein', 'Carbs', 'Chất béo', 'Chất xơ'])
        stats=[80, 90, 75, 85, 70]
        
        angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        stats=np.concatenate((stats,[stats[0]]))
        angles=np.concatenate((angles,[angles[0]]))
        
        ax2 = plt.subplot(111, polar=True)
        ax2.plot(angles, stats, 'o-', linewidth=2, color='#ff6e40')
        ax2.fill(angles, stats, alpha=0.25, color='#ff6e40')
        ax2.set_thetagrids(angles[:-1] * 180/np.pi, labels)
        ax2.set_ylim(0,100)
        st.pyplot(fig2)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("⚠️ Hạn chế của Mô hình & Hướng Cải tiến")
    st.markdown("""
    **Hạn chế:**
    * **Kích thước Dữ liệu:** Tập dữ liệu hiện tại chứa số lượng món ăn hạn chế, có thể dẫn đến các thực đơn bị lặp lại.
    * **Độ phức tạp của CSP:** Bộ giải CSP hiện tại sử dụng phương pháp lấy mẫu ngẫu nhiên heuristic. Mặc dù nhanh, nhưng nó không đảm bảo tìm ra giải pháp tối ưu toàn cục tuyệt đối.
    * **Vi chất dinh dưỡng:** Mô hình hiện tại tập trung vào các chất dinh dưỡng đa lượng và một vài vi chất (natri, đường). Nó thiếu theo dõi các loại vitamin và khoáng chất.
    
    **Hướng Cải tiến:**
    * **Bộ giải CSP Nâng cao:** Triển khai các thuật toán phức tạp hơn như Forward Checking hoặc AC-3 để thỏa mãn ràng buộc chính xác.
    * **Tích hợp Học máy (Machine Learning):** Sử dụng lọc cộng tác (collaborative filtering) hoặc học sâu (deep learning) để học sở thích của người dùng theo thời gian.
    * **Tích hợp API:** Kết nối với các cơ sở dữ liệu thực phẩm bên ngoài (ví dụ: USDA FoodData Central hoặc Edamam) để có sự đa dạng thực phẩm lớn hơn rất nhiều.
    """)

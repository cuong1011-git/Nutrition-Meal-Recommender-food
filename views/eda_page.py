import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def show_eda_page(df):
    st.title("🥗 Ứng dụng AI Gợi ý Thực đơn Dinh dưỡng Cá nhân hóa")
    st.markdown("### Sử dụng Lọc Dựa trên Luật (Rule-Based) và Bài toán Thỏa mãn Ràng buộc (CSP)")
    
    st.markdown("---")
    col_info1, col_info2 = st.columns(2)
    with col_info1:
        st.write("**Tên sinh viên:** Nguyễn Quốc Cường")
    with col_info2:
        st.write("**Mã sinh viên:** 22T1020558")
    st.markdown("---")
    
    st.markdown("""
    ### 🌟 Tầm quan trọng của Dinh dưỡng Cá nhân hóa
    Dinh dưỡng cá nhân hóa đóng vai trò thiết yếu trong việc quản lý tình trạng sức khỏe, tối ưu hóa thể trạng và phòng ngừa các bệnh mãn tính. 
    Bằng cách điều chỉnh thực đơn phù hợp với chỉ số cơ thể và tiền sử bệnh lý của từng cá nhân, chúng ta có thể cải thiện đáng kể kết quả sức khỏe.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📊 Xem trước Dữ liệu")
    st.dataframe(df.head(10), use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📈 Phân tích Dữ liệu Khám phá (EDA)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Phân bố Danh mục Thực phẩm**")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.countplot(data=df, x='category', palette='Set2', ax=ax)
        ax.set_xlabel("Danh mục")
        ax.set_ylabel("Số lượng")
        plt.xticks(rotation=45)
        st.pyplot(fig)
        st.caption("Sự phân bố của các món ăn qua các bữa ăn khác nhau.")
        
    with col2:
        st.markdown("**Ma trận Tương quan Dinh dưỡng**")
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        nutrients = df[['calories', 'protein', 'fat', 'carbohydrates', 'sugar', 'sodium', 'fiber']]
        sns.heatmap(nutrients.corr(), annot=True, cmap='YlGnBu', fmt=".2f", ax=ax2, cbar=False)
        st.pyplot(fig2)
        st.caption("Mối tương quan giữa các thành phần dinh dưỡng khác nhau.")

import streamlit as st
from utils.nutrition_calculator import calculate_bmi, calculate_daily_calories, get_nutritional_constraints
from utils.rule_based_filter import apply_rules
from utils.csp_solver import solve_csp

def show_recommendation_page(df):
    st.title("🍽️ Gợi ý Thực đơn")
    st.markdown("Nhập thông tin cá nhân của bạn để nhận thực đơn được tối ưu hóa bằng AI.")
    
    st.sidebar.header("👤 Thông tin Cá nhân")
    age = st.sidebar.number_input("Tuổi", min_value=10, max_value=100, value=30)
    gender = st.sidebar.selectbox("Giới tính", ["Nam", "Nữ"])
    # Map back to English for calculation
    gender_en = "Male" if gender == "Nam" else "Female"
    
    height = st.sidebar.number_input("Chiều cao (cm)", min_value=100, max_value=250, value=170)
    weight = st.sidebar.number_input("Cân nặng (kg)", min_value=30, max_value=200, value=70)
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("🏥 Tình trạng Bệnh lý")
    diabetes = st.sidebar.checkbox("Tiểu đường")
    hypertension = st.sidebar.checkbox("Huyết áp cao")
    heart_disease = st.sidebar.checkbox("Bệnh tim mạch")
    obesity = st.sidebar.checkbox("Béo phì")
    
    if st.sidebar.button("Tạo Thực Đơn Ngay 🚀"):
        st.markdown("---")
        
        # 1. Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # 2. Calculate Needs
        daily_calories = calculate_daily_calories(age, gender_en, weight, height)
        constraints = get_nutritional_constraints(daily_calories, diabetes, hypertension, obesity, heart_disease)
        
        col_metrics1, col_metrics2 = st.columns(2)
        with col_metrics1:
            st.metric("Chỉ số BMI của bạn", f"{bmi:.2f}")
        with col_metrics2:
            st.metric("Mục tiêu Calo Hàng ngày", f"{daily_calories:.0f} kcal")
        
        # 3. Apply Rule-Based Filtering
        filtered_df = apply_rules(df, diabetes, hypertension, obesity, heart_disease)
        st.info(f"🔍 **Lọc Dựa trên Luật:** Đã tìm thấy {len(filtered_df)} / {len(df)} món ăn phù hợp với tình trạng sức khỏe của bạn.")
        
        # 4. Run CSP Meal Planner
        with st.spinner("🧠 Đang tối ưu hóa thực đơn bằng thuật toán CSP..."):
            meal_plan = solve_csp(filtered_df, constraints)
            
        # 5. Output Recommended Meals
        if meal_plan:
            if meal_plan.get('relaxed'):
                st.warning("⚠️ Không thể tìm thấy thực đơn đáp ứng hoàn hảo tất cả các ràng buộc nghiêm ngặt. Hiển thị lựa chọn gần nhất dựa trên các thực phẩm đã lọc.")
            else:
                st.success("✅ Đã tạo thành công thực đơn đáp ứng tất cả các ràng buộc dinh dưỡng và bệnh lý!")
                
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("🍱 Thực Đơn Đề Xuất Cho Bạn")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f"""
                <div class="meal-card">
                    <div class="meal-title">🍳 Bữa Sáng</div>
                    <div class="meal-food">{meal_plan['breakfast']['food_name']}</div>
                    <div class="meal-cal">🔥 {meal_plan['breakfast']['calories']} kcal</div>
                </div>
                """, unsafe_allow_html=True)
                
            with col2:
                st.markdown(f"""
                <div class="meal-card">
                    <div class="meal-title">🥗 Bữa Trưa</div>
                    <div class="meal-food">{meal_plan['lunch']['food_name']}</div>
                    <div class="meal-cal">🔥 {meal_plan['lunch']['calories']} kcal</div>
                </div>
                """, unsafe_allow_html=True)
                
            with col3:
                st.markdown(f"""
                <div class="meal-card">
                    <div class="meal-title">🍲 Bữa Tối</div>
                    <div class="meal-food">{meal_plan['dinner']['food_name']}</div>
                    <div class="meal-cal">🔥 {meal_plan['dinner']['calories']} kcal</div>
                </div>
                """, unsafe_allow_html=True)
                
            if meal_plan.get('snack'):
                st.markdown(f"""
                <div class="meal-card" style="max-width: 33%; margin: 0 auto;">
                    <div class="meal-title">🍎 Bữa Phụ (Ăn vặt)</div>
                    <div class="meal-food">{meal_plan['snack']['food_name']}</div>
                    <div class="meal-cal">🔥 {meal_plan['snack']['calories']} kcal</div>
                </div>
                """, unsafe_allow_html=True)
                
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("📊 Tổng Giá trị Dinh dưỡng")
            totals = meal_plan['totals']
            
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Tổng Calo", f"{totals['calories']:.0f} kcal", f"Tối đa: {constraints['max_calories']:.0f}", delta_color="inverse")
            m2.metric("Tổng Protein", f"{totals['protein']:.0f} g", f"Tối thiểu: {constraints['min_protein']:.0f}", delta_color="normal")
            m3.metric("Tổng Đường", f"{totals['sugar']:.0f} g", f"Tối đa: {constraints['max_sugar']:.0f}", delta_color="inverse")
            m4.metric("Tổng Natri", f"{totals['sodium']:.0f} mg", f"Tối đa: {constraints['max_sodium']:.0f}", delta_color="inverse")
            
        else:
            st.error("❌ Không có thực phẩm phù hợp cho các tình trạng sức khỏe đã chọn. Vui lòng điều chỉnh ràng buộc hoặc thêm thực phẩm vào cơ sở dữ liệu.")

import streamlit as st
import pickle 
import os
from streamlit_option_menu import option_menu 

st.set_page_config(page_title="Multiple Disease Predictor",layout="wide",page_icon="🤖")

working_dir = os.path.dirname(os.path.abspath(__file__))
heart_model = pickle.load(open(f'{working_dir}/saved_models\heart (2).pkl','rb'))
kidney_model= pickle.load(open(f'{working_dir}/saved_models\kindey.pkl','rb'))

with st.sidebar:
    selected = option_menu("Multiple Disease Prediction using Machine Learning",
                ['Heart disease predictor',
                 'Kidney disease predictor'],
                 menu_icon='hospital-fill',
                 icons=['activity','heart','person'],
                 default_index=0)

if selected == 'Heart disease predictor':
    st.title("Diabetes Prediction using Machine Learning")
    col1 , col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex")
    with col3:
        cp = st.text_input("CP")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Chlorestrol")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar")
    with col1:
        restecg = st.text_input("Resting Electrocardiography")
    with col2:
        thalach = st.text_input("THALAC")
    with col3:
        exang = st.text_input("Exercise Enduced Angima")
    with col1:
        oldpeak = st.text_input("ST Depression")
    with col2:
        slope = st.text_input("ST peak exercise")
    with col3:
        ca = st.text_input("CA")
    with col1:
        thal = st.text_input("Thal")
    
    heart_result = ""
    if st.button("Test Result"):
        user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input = [float(x) for x in user_input]
        prediction = heart_model.predict([user_input])
        if (prediction [0] == 1):
            st.error(" You are having a Heart disease") # Using st.error makes the result stand out in red
            
            # --- NEW FEATURES START HERE ---
            st.subheader("💡 Health & Wellness Suggestions")
            
            col_yoga, col_activity = st.columns(2)
            
            with col_yoga:
                st.markdown("#### 🧘 Recommended Yoga")
                
                # Tadasana
                st.write("* **Tadasana** (Mountain Pose)")
                st.video("http://www.youtube.com/watch?v=5NxDs-ovJU8")
                
                # Vrikshasana
                st.write("* **Vrikshasana** (Tree Pose)")
                st.video("http://www.youtube.com/watch?v=uELr6MPi7pI")
                
                # Shavasana
                st.write("* **Shavasana** (Corpse Pose)")
                st.video("http://www.youtube.com/watch?v=9ZsTLblha9o")

            with col_activity:
                st.markdown("#### 🚶 Physical Activities")
                st.write("* **Brisk Walking** (30 mins/day)")
                st.write("* **Cycling** at a moderate pace")
                st.write("* **Swimming** (low impact on joints)")

            st.divider()

            # --- NEW DIETARY SECTION ---
            st.subheader("🥗 Dietary Recommendations")
            
            col_eat, col_avoid = st.columns(2)
            with col_eat:
                st.success("✅ **Foods to Consume**")
                st.write("* **Leafy Greens:** Spinach, Kale, and Fenugreek (Methi).")
                st.write("* **Whole Grains:** Oats, Brown Rice, and Whole Wheat.")
                st.write("* **Healthy Fats:** Walnuts, Almonds, and Olive Oil.")
                st.write("* **Fruits:** Apples, Oranges, and Berries.")

            with col_avoid:
                st.warning("❌ **Foods to Avoid**")
                st.write("* **High Sodium:** Table salt, Canned soups, and Pickles.")
                st.write("* **Processed Meats:** Sausages, Salami, and Bacon.")
                st.write("* **Trans Fats:** Fried fast foods and Packaged snacks.")
                st.write("* **Added Sugars:** Soda, Energy drinks, and Sweets.")

            st.divider()
            
            st.markdown("#### 🏥 Find Nearby Help")
            st.info("Please consult a cardiologist immediately. You can find nearby hospitals using the link below:")
            # This creates a clickable link that opens Google Maps for hospitals near the user
            st.markdown("[Click here to find nearby Cardiology Hospitals](https://www.google.com/maps/search/cardiology+hospitals+near+me/)")

            st.divider()
            st.subheader("💰 Government Healthcare Financial Aid")
            st.info("If you are from a low-income background, you may be eligible for free or subsidized treatment.")

            col_scheme1, col_scheme2 = st.columns(2)
            
            with col_scheme1:
                st.markdown("#### 🇮🇳 Ayushman Bharat (PM-JAY)")
                st.write("Provides up to ₹5 Lakh per family per year for secondary and tertiary care hospitalization.")
                st.markdown("[Check Eligibility & Apply Here](https://dashboard.pmjay.gov.in/pmjayportal/aadhaarsearch)")

            with col_scheme2:
                st.markdown("#### 🏥 RAN (Rashtriya Arogya Nidhi)")
                st.write("Provides one-time financial assistance to patients living below the poverty line for life-threatening diseases.")
                st.markdown("[Learn More About RAN Scheme](https://main.mohfw.gov.in/Major-Programmes/poor-patients-financial-assistance/rashtriya-arogya-nidhi)")

            # General link for all State Government schemes
            st.markdown("---")
            st.write("🔍 **Looking for state-specific help?**")
            st.markdown("[View All State Health Insurance Schemes](https://www.nhp.gov.in/health-insurance-schemes_pg)")
            
            # --- NEW FEATURES END HERE ---

        
        else:
            st.success("Great news! Your results indicate you are currently healthy.")
            st.balloons() 
            
            st.subheader("🌟 Maintain Your Good Health")
            st.info("Prevention is better than cure. Follow these tips to stay fit!")

            # --- PREVENTIVE LIFESTYLE ---
            col_yoga, col_diet = st.columns(2)
            
            with col_yoga:
                st.markdown("#### 🧘 Daily Yoga & Activity")
                
                # Surya Namaskar - General Wellness
                st.write("**1. Surya Namaskar** (Sun Salutation)")
                st.video("https://www.youtube.com/watch?v=y_1XREpWvK0")
                
                # Pranayama - Stress & Respiratory Health
                st.write("**2. Pranayama** (Breathing Exercises)")
                st.video("https://www.youtube.com/watch?v=3S_v7R-t7Y4")
                
                st.write("* **Activity:** At least 30 mins of daily movement (walking/dancing).")

            with col_diet:
                st.markdown("#### 🥗 Healthy Diet Habits")
                st.write("* **Hydration:** Drink 8-10 glasses of water daily.")
                st.write("* **Fiber:** Include more seasonal fruits and raw salads.")
                st.write("* **Portion Control:** Avoid overeating, especially at dinner.")
                st.write("* **Limit Sugar:** Reduce intake of processed sweets and sodas.")

            st.divider()

            # --- DO'S AND DON'TS ---
            col_do, col_dont = st.columns(2)
            
            with col_do:
                st.success("✅ **Do's**")
                st.write("* Get 7-8 hours of quality sleep.")
                st.write("* Practice mindfulness or meditation.")
                st.write("* Regular health checkups once a year.")

            with col_dont:
                st.warning("❌ **Don'ts**")
                st.write("* Avoid long hours of sitting (take breaks).")
                st.write("* Stop smoking and limit alcohol.")
                st.write("* Don't ignore minor symptoms if they persist.")

if selected == 'Kidney disease predictor':
    st.title("Kidney Disease Prediction using Machine Learning")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        age = st.text_input("Age")
    with col2:
        bp = st.text_input("Blood Pressure")
    with col3:
        sg = st.text_input("Specific Gravity (of urine)")
    with col4:
        al = st.text_input("Albumin (in urine)")
    with col5:
        su = st.text_input("Sugar")
    with col1:
        rbc = st.text_input("Red Blood Cell count")
    with col2:
        pc = st.text_input("Pus cell")
    with col3:
        pcc = st.text_input("Pus cell clumps")
    with col4:
        ba = st.text_input("Bacteria")
    with col5:
        bgr = st.text_input("Blood Glucose Randome")
    with col1:
        bu = st.text_input("blood urea")
    with col2:
        sc = st.text_input("Serum Creatinine")
    with col3:
        sod = st.text_input("Sodium")
    with col4:
        pot = st.text_input("Potassium")
    with col5:
        hemo = st.text_input("Haemoglobin")
    with col1:
        pcv = st.text_input("Packed Cell Volume")
    with col2:
        wc = st.text_input("White Blood Cell Count")
    with col3:
        rc = st.text_input("Red Blod Cell count")
    with col4:
        htn = st.text_input("Hypertension")
    with col5:
        dm = st.text_input("Diabetes Mellitus")
    with col1:
        cad = st.text_input("Coronary Artery Disease")
    with col2:
        appet = st.text_input("Appetite")
    with col3:
        pe = st.text_input("Peda edema")
    with col4:
        ane = st.text_input("Anaemia")
    
    
    # code for Prediction
    kindey_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Test Result"):

        user_input = [age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]

        user_input = [float(x) for x in user_input]

        prediction = kidney_model.predict([user_input])

        if (prediction[0] == 1):
            
            st.error("You have a Kidney Disease")

            # --- NEW KIDNEY HEALTH SUGGESTIONS ---
            st.subheader("💡 Kidney Care & Wellness")

            col_yoga = st.columns(1)
            
            with col_yoga:
                st.markdown("#### 🧘 Recommended Yoga")
                
                # Tadasana
                st.write("* **Tadasana** (Mountain Pose)")
                st.video("http://www.youtube.com/watch?v=5NxDs-ovJU8")
                
                # Vrikshasana
                st.write("* **Vrikshasana** (Tree Pose)")
                st.video("http://www.youtube.com/watch?v=uELr6MPi7pI")
                
                # Shavasana
                st.write("* **Shavasana** (Corpse Pose)")
                st.video("http://www.youtube.com/watch?v=9ZsTLblha9o")
            
            col_activity, col_hospitals = st.columns(2)
            with col_activity:
                st.markdown("#### 🏃 Lifestyle Habits")
                st.write("* **Stay Hydrated:** Drink water as advised by your doctor.")
                st.write("* **Monitor BP:** Keep track of your blood pressure daily.")
                st.write("* **Quit Smoking:** Smoking reduces blood flow to kidneys.")

            with col_hospitals:
                st.markdown("#### 🏥 Medical Assistance")
                st.write("* Consult a **Nephrologist** immediately.")
                st.markdown("[Find Kidney Specialist Hospitals](https://www.google.com/maps/search/nephrologist+near+me)")

            st.divider()

            # --- DIETARY RECOMMENDATIONS FOR KIDNEY ---
            st.subheader("🥗 Renal (Kidney) Diet Guide")
            
            col_eat, col_avoid = st.columns(2)
            with col_eat:
                st.success("✅ **Foods to Consume**")
                st.write("* **Cauliflower & Cabbage:** Low in potassium.")
                st.write("* **Blueberries:** High in antioxidants, low in sodium.")
                st.write("* **Egg Whites:** High-quality, kidney-safe protein.")
                st.write("* **Garlic & Onion:** Great flavor without using salt.")

            with col_avoid:
                st.warning("❌ **Foods to Avoid**")
                st.write("* **High Potassium:** Bananas, Potatoes, and Spinach.")
                st.write("* **High Phosphorus:** Dark sodas, Nuts, and Dairy.")
                st.write("* **Processed Salt:** Chips, Instant noodles, and Pickles.")
                st.write("* **Red Meat:** Can be hard for damaged kidneys to process.")
            
            st.info("⚠️ **Note:** Kidney diets are very specific. Please consult a renal dietitian.")

            st.divider()
            st.subheader("💰 Government Healthcare Financial Aid")
            st.info("If you are from a low-income background, you may be eligible for free or subsidized treatment.")

            col_scheme1, col_scheme2 = st.columns(2)
            
            with col_scheme1:
                st.markdown("#### 🇮🇳 Ayushman Bharat (PM-JAY)")
                st.write("Provides up to ₹5 Lakh per family per year for secondary and tertiary care hospitalization.")
                st.markdown("[Check Eligibility & Apply Here](https://dashboard.pmjay.gov.in/pmjayportal/aadhaarsearch)")

            with col_scheme2:
                st.markdown("#### 🏥 RAN (Rashtriya Arogya Nidhi)")
                st.write("Provides one-time financial assistance to patients living below the poverty line for life-threatening diseases.")
                st.markdown("[Learn More About RAN Scheme](https://main.mohfw.gov.in/Major-Programmes/poor-patients-financial-assistance/rashtriya-arogya-nidhi)")

            # General link for all State Government schemes
            st.markdown("---")
            st.write("🔍 **Looking for state-specific help?**")
            st.markdown("[View All State Health Insurance Schemes](https://www.nhp.gov.in/health-insurance-schemes_pg)")

            # --- END OF NEW FEATURES ---

        else:
            st.success("Great news! Your results indicate your kidneys are currently healthy.")
            st.balloons() 
            
            st.subheader("🌟 Protect Your Kidney Health")
            st.info("The kidneys filter your blood 24/7. Here is how to keep them running smoothly!")

            # --- PREVENTIVE KIDNEY CARE ---
            col_yoga, col_diet = st.columns(2)
            
            with col_yoga:
                st.markdown("#### 🧘 Yoga for Kidney Detox")
                
                # Bhujangasana - Excellent for renal blood flow
                st.write("**1. Bhujangasana** (Cobra Pose)")
                st.video("https://www.youtube.com/watch?v=Lfd0HT2dr6Y")
                
                # Paschimottanasana - Stretches and stimulates the kidneys
                st.write("**2. Paschimottanasana** (Seated Forward Bend)")
                st.video("https://www.youtube.com/watch?v=faS62Kftifw")
                
                st.write("* **Daily Step Goal:** Walk 7,000-10,000 steps to maintain blood pressure.")

            with col_diet:
                st.markdown("#### 🥗 Renal-Friendly Habits")
                st.write("* **Water is Key:** Drink enough to keep your urine pale yellow.")
                st.write("* **Reduce Salt:** High salt is the #1 enemy of kidneys.")
                st.write("* **Limit Painkillers:** Overuse of NSAIDs (like Ibuprofen) can damage kidneys.")
                st.write("* **Control Sugar:** High blood sugar is a leading cause of kidney issues.")
                
                st.write("#### 🎥 Kidney Health Tips")
                st.video("https://www.youtube.com/watch?v=mz3_jLQe9r8") # Quick food tips for kidneys

            st.divider()

            # --- PREVENTIVE DO'S AND DON'TS ---
            col_do, col_dont = st.columns(2)
            
            with col_do:
                st.success("✅ **Do's**")
                st.write("* Monitor your blood pressure regularly.")
                st.write("* Eat more antioxidants (Berries, Bell peppers).")
                st.write("* Stay at a healthy weight.")

            with col_dont:
                st.warning("❌ **Don'ts**")
                st.write("* Don't hold your urine for long periods.")
                st.write("* Avoid excessive intake of protein supplements.")
                st.write("* Stop smoking (it slows blood flow to kidneys).")
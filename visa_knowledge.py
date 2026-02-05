def get_visa_response(user_input):
    user_input = user_input.lower()

    if "uk" in user_input and "student" in user_input:
        return (
            "🇬🇧 UK Student Visa (Step-by-Step):\n\n"
            "1. Get CAS letter from UK university\n"
            "2. Apply online on UKVI portal\n"
            "3. Pay visa fee and health surcharge\n"
            "4. Book biometric appointment\n"
            "5. Attend appointment\n"
            "6. Wait for decision\n\n"
            "📄 Documents:\n"
            "- Passport\n"
            "- CAS letter\n"
            "- Financial proof\n"
            "- English test result\n\n"
            "🔗 Official Link:\n"
            "https://www.gov.uk/student-visa"
        )

    elif "germany" in user_input and "student" in user_input:
        return (
            "🇩🇪 Germany Student Visa:\n\n"
            "1. Secure university admission\n"
            "2. Open blocked account\n"
            "3. Buy health insurance\n"
            "4. Book visa appointment\n"
            "5. Attend interview\n\n"
            "🔗 Official Links:\n"
            "https://www.auswaertiges-amt.de\n"
            "https://www.vfsglobal.com"
        )

    elif "usa" in user_input and ("student" in user_input or "f1" in user_input):
        return (
            "🇺🇸 USA F-1 Student Visa:\n\n"
            "1. Get I-20 from university\n"
            "2. Pay SEVIS fee\n"
            "3. Fill DS-160 form\n"
            "4. Pay visa fee\n"
            "5. Attend interview\n\n"
            "🔗 Official Links:\n"
            "https://travel.state.gov\n"
            "https://www.ustraveldocs.com"
        )

    elif "documents" in user_input:
        return (
            "📄 Common Student Visa Documents:\n"
            "- Passport\n"
            "- Admission letter\n"
            "- Financial proof\n"
            "- Academic certificates\n"
            "- Health insurance"
        )

    else:
        return (
            "🤖 I can help with:\n"
            "- UK / USA / Germany student visas\n"
            "- Documents required\n"
            "- Step-by-step application process\n\n"
            "Example:\n"
            "'How to apply for UK student visa?'"
        )

# Coffee Disease Expert System - Internationalization (i18n)
# Supports Khmer (km) and English (en)

TRANSLATIONS = {
    'km': {
        # App Branding & Navigation
        'app_title': 'ប្រព័ន្ធអ្នកជំនាញជំងឺដើមកាហ្វេ',
        'app_brand': 'ប្រព័ន្ធជំងឺដើមកាហ្វេ',
        'dashboard': 'ផ្ទាំងគ្រប់គ្រង',
        'diagnose': 'វិនិច្ឆ័យជំងឺ',
        'cases_history': 'ប្រវត្តិករណី',
        'rules_management': 'គ្រប់គ្រងច្បាប់',
        'users': 'អ្នកប្រើប្រាស់',
        'my_profile': 'គណនីរបស់ខ្ញុំ (Profile)',
        'logout': 'ចាកចេញ',
        'login': 'ចូលប្រើប្រាស់',
        'register': 'ចុះឈ្មោះគណនី',
        'forgot_password': 'ភ្លេចពាក្យសម្ងាត់',
        'language': 'ភាសា',
        'lang_km': 'ភាសាខ្មែរ',
        'lang_en': 'English',

        # Dashboard
        'hello': 'សួស្តី',
        'welcome_subtitle_admin': 'គ្រប់គ្រង និងតាមដានរាល់សកម្មភាពវិនិច្ឆ័យ មូលដ្ឋានចំណេះដឹង និងគណនីអ្នកប្រើប្រាស់ទូទាំងប្រព័ន្ធ',
        'welcome_subtitle_user': 'តាមដានសុខភាពដំណាំកាហ្វេរបស់អ្នក ពិនិត្យមើលរោគសញ្ញា និងស្វែងរកវិធីព្យាបាលទាន់ពេលវេលា',
        'admin_badge': 'ផ្ទាំងគ្រប់គ្រង Admin',
        'user_badge': 'កសិករ / អ្នកប្រើប្រាស់',
        'new_diagnosis_btn': 'វិនិច្ឆ័យជំងឺថ្មី',
        'total_cases_admin': 'ករណីសរុបក្នុងប្រព័ន្ធ',
        'total_cases_user': 'ករណីវិនិច្ឆ័យសរុប',
        'system_wide': 'ប្រព័ន្ធទាំងមូល',
        'personal_cases': 'ករណីផ្ទាល់ខ្លួន',
        'month_cases_admin': 'ករណីខែនេះ (ប្រព័ន្ធ)',
        'month_cases_user': 'ករណីខែនេះរបស់អ្នក',
        'current_month': 'ខែបច្ចុប្បន្ន',
        'avg_confidence': 'ភាពជឿជាក់មធ្យម',
        'knowledge_base': 'មូលដ្ឋានទិន្នន័យ',
        'diseases_unit': 'ជំងឺ',
        'symptoms_unit': 'រោគសញ្ញា',
        
        # Action Tiles
        'tile_diagnose_title': 'វិនិច្ឆ័យជំងឺ',
        'tile_diagnose_desc_admin': 'ដំណើរការវិភាគដោយ Forward Chaining',
        'tile_diagnose_desc_user': 'ជ្រើសរើសរោគសញ្ញាដែលកើតមានលើដើមកាហ្វេ',
        'tile_cases_title_admin': 'ប្រវត្តិករណីសរុប',
        'tile_cases_title_user': 'ប្រវត្តិករណីរបស់ខ្ញុំ',
        'tile_cases_desc_admin': 'ពិនិត្យតាមដានករណីរបស់អ្នកប្រើទាំងអស់',
        'tile_cases_desc_user': 'ពិនិត្យមើលលទ្ធផល និងវិធីព្យាបាលពីមុនៗ',
        'tile_rules_title': 'គ្រប់គ្រងច្បាប់',
        'tile_rules_desc': 'កំណត់រចនាសម្ព័ន្ធជំងឺ រោគសញ្ញា និងទម្ងន់ច្បាប់',
        'tile_users_title': 'អ្នកប្រើប្រាស់',
        'tile_users_desc': 'គ្រប់គ្រងគណនី សិទ្ធិ និងតួនាទីក្នុងប្រព័ន្ធ',
        'tile_profile_title': 'គណនីផ្ទាល់ខ្លួន',
        'tile_profile_desc': 'កែប្រែព័ត៌មាន និងផ្លាស់ប្តូរពាក្យសម្ងាត់',

        # Tables & Lists
        'recent_cases_admin': 'ករណីវិនិច្ឆ័យថ្មីៗក្នុងប្រព័ន្ធ',
        'recent_cases_user': 'ករណីវិនិច្ឆ័យថ្មីៗរបស់អ្នក',
        'view_all': 'មើលទាំងអស់',
        'th_date': 'កាលបរិច្ឆេទ',
        'th_user': 'កសិករ / អ្នកប្រើប្រាស់',
        'th_disease': 'ជំងឺដែលវិនិច្ឆ័យបាន',
        'th_confidence': 'កម្រិតភាពជឿជាក់',
        'th_location': 'ទីតាំងចម្ការ',
        'th_actions': 'សកម្មភាព',
        'no_recent_cases': 'មិនទាន់មានករណីវិនិច្ឆ័យនៅឡើយទេ',
        'start_first_diag': 'ចាប់ផ្តើមវិនិច្ឆ័យដំបូង',
        'view_details': 'មើលលម្អិត',
        'delete': 'លុប',
        'delete_confirm': 'តើអ្នកប្រាកដជាចង់លុបករណីវិនិច្ឆ័យនេះមែនទេ?',
        'unspecified': 'មិនបានបញ្ជាក់',
        'case_details_modal_title': 'ព័ត៌មានលម្អិតនៃករណី',
        'treatment_label': 'ការព្យាបាល៖',
        'prevention_label': 'ការការពារ៖',
        'notes_label': 'កំណត់ចំណាំ៖',
        'analysis_results_heading': 'លទ្ធផលនៃការវិភាគ៖',
        'no_detailed_results': 'គ្មានលទ្ធផលលម្អិត',

        # Diagnosis Page
        'diag_header_title': 'ប្រព័ន្ធវិនិច្ឆ័យជំងឺដំណាំកាហ្វេ',
        'diag_header_subtitle': 'សូមជ្រើសរើសរោគសញ្ញាជាក់ស្តែងដែលអ្នកបានសង្កេតឃើញលើដើមកាហ្វេរបស់អ្នក',
        'all_categories': 'ទាំងអស់',
        'cat_leaf': 'ស្លឹក (Leaves)',
        'cat_stem': 'ដើម & មែក (Stems)',
        'cat_root': 'ឫស (Roots)',
        'cat_fruit': 'ផ្លែ (Berries)',
        'search_symptoms_placeholder': 'ស្វែងរករោគសញ្ញា (ឧ. ស្លឹកលឿង, ឫសរលួយ...)',
        'selected_symptoms_badge': 'បានជ្រើសរើស',
        'clear_all': 'សម្អាតទាំងអស់',
        'farm_location': 'ទីតាំងចម្ការកាហ្វេ',
        'farm_location_placeholder': 'ឧ. មណ្ឌលគិរី, រតនគិរី, ប៉ៃលិន...',
        'farm_notes': 'កំណត់ចំណាំបន្ថែម',
        'farm_notes_placeholder': 'ព័ត៌មានបន្ថែមអំពីអាយុកាលដំណាំ ការស្រោចទឹក ឬជី...',
        'submit_diagnosis_btn': 'ដំណើរការវិនិច្ឆ័យជំងឺ',
        'diag_result_title': 'លទ្ធផលនៃការវិនិច្ឆ័យជំងឺ',
        'no_disease_matched_title': 'មិនអាចកំណត់ជំងឺបានជាក់លាក់',
        'no_disease_matched_desc': 'រោគសញ្ញាដែលបានជ្រើសរើសមិនទាន់គ្រប់គ្រាន់ដើម្បីផ្គូផ្គងនឹងជំងឺណាមួយឡើយ។ សូមជ្រើសរើសរោគសញ្ញាបន្ថែម។',
        'run_new_diag': 'វិនិច្ឆ័យករណីថ្មី',
        'diag_stepper_1': '១. សង្កេតរោគសញ្ញា',
        'diag_stepper_2': '២. ព័ត៌មានចម្ការ',
        'diag_stepper_3': '៣. វិភាគ & ព្យាបាល',
        'symptoms_catalog': 'កាតាឡុកនៃរោគសញ្ញាជាក់ស្តែង',
        'symptoms_catalog_sub': 'ជ្រើសរើសរោគសញ្ញាទាំងអស់ដែលត្រូវគ្នានឹងដើមកាហ្វេរបស់អ្នក',
        'select_all_btn': 'ជ្រើសទាំងអស់',
        'deselect_all_btn': 'ដោះទាំងអស់',
        'selected_tray_title': 'រោគសញ្ញាដែលបានជ្រើសរើស',
        'selected_tray_empty': 'មិនទាន់មានរោគសញ្ញាដែលបានជ្រើសរើសនៅឡើយ។ សូមចុចលើកាតរោគសញ្ញាខាងឆ្វេងដើម្បីជ្រើសរើស។',
        'quick_location_label': 'ទីតាំងរហ័ស៖',
        'sys_specs_title': 'លក្ខណៈបច្ចេកទេសប្រព័ន្ធ',
        'sys_specs_algo': 'ក្បួនដោះស្រាយ៖',
        'sys_specs_algo_val': 'Forward Chaining + CF',
        'sys_specs_kb': 'មូលដ្ឋានទិន្នន័យ៖',
        'sys_specs_kb_val': '១៥ ជំងឺ & ១៧ រោគសញ្ញា',
        'sys_specs_engine': 'ម៉ាស៊ីនវិភាគ៖',
        'sys_specs_engine_val': 'Expert Rules Weighted Engine',
        'inspection_guide_title': 'គោលការណ៍ត្រួតពិនិត្យដំណាំ',
        'diff_diagnoses_title': 'ជម្រើសជំងឺបន្ទាប់បន្សំ (Differential Diagnoses)',
        'print_report_btn': 'បោះពុម្ពរបាយការណ៍',
        'save_history_btn': 'មើលក្នុងប្រវត្តិករណី',

        # Cases History Page
        'cases_page_title': 'ប្រវត្តិករណីវិនិច្ឆ័យ',
        'cases_page_subtitle': 'ពិនិត្យ និងតាមដានរាល់ករណីវិនិច្ឆ័យជំងឺដែលបានរក្សាទុកក្នុងប្រព័ន្ធ',
        'search_cases_placeholder': 'ស្វែងរកតាមឈ្មោះជំងឺ ទីតាំង...',
        'period_all': 'ទាំងអស់',
        'period_today': 'ថ្ងៃនេះ',
        'period_week': '៧ ថ្ងៃចុងក្រោយ',
        'period_month': '៣០ ថ្ងៃចុងក្រោយ',
        'no_cases_period': 'មិនមានប្រវត្តិករណីសម្រាប់ពេលវេលាដែលបានជ្រើសរើសទេ',

        # Profile Page
        'profile_title': 'គណនីផ្ទាល់ខ្លួន',
        'diagnoses_count_label': 'ករណីវិនិច្ឆ័យ',
        'account_status_label': 'ស្ថានភាពគណនី',
        'active_status': 'សកម្ម (Active)',
        'security_tips_title': 'ព័ត៌មានជំនួយសុវត្ថិភាព',
        'tip_length': 'ប្រើប្រាស់ពាក្យសម្ងាត់ដែលមានប្រវែងយ៉ាងតិច ៦ តួអក្សរ។',
        'tip_share': 'កុំចែករំលែកព័ត៌មានសម្ងាត់របស់អ្នកទៅកាន់អ្នកដទៃ។',
        'tip_change': 'ផ្លាស់ប្តូរពាក្យសម្ងាត់ជាប្រចាំដើម្បីធានាសុវត្ថិភាពគណនី។',
        'edit_account_title': 'កែប្រែព័ត៌មានគណនី',
        'username_label': 'ឈ្មោះអ្នកប្រើប្រាស់ (Username)',
        'username_cannot_change': 'មិនអាចផ្លាស់ប្តូរឈ្មោះសម្គាល់បានទេ',
        'role_label': 'តួនាទី (Role)',
        'role_admin_managed': 'កំណត់ដោយអ្នកគ្រប់គ្រងប្រព័ន្ធ',
        'full_name_label': 'ឈ្មោះពេញ (Full Name)',
        'email_label': 'អាសយដ្ឋានអ៊ីមែល (Email)',
        'save_changes_btn': 'រក្សាទុកការផ្លាស់ប្តូរ',
        'change_password_title': 'ផ្លាស់ប្តូរពាក្យសម្ងាត់',
        'current_password_label': 'ពាក្យសម្ងាត់បច្ចុប្បន្ន (Current Password)',
        'new_password_label': 'ពាក្យសម្ងាត់ថ្មី (New Password)',
        'confirm_password_label': 'បញ្ជាក់ពាក្យសម្ងាត់ថ្មី (Confirm Password)',
        'min_6_chars_placeholder': 'យ៉ាងតិច ៦ តួអក្សរ',
        'update_password_btn': 'កំណត់ពាក្យសម្ងាត់ថ្មី',

        # Rules Management
        'rules_title': 'គ្រប់គ្រងមូលដ្ឋានចំណេះដឹង',
        'rules_subtitle': 'កំណត់រចនាសម្ព័ន្ធជំងឺ រោគសញ្ញា និងច្បាប់វិភាគ Forward Chaining',
        'tab_diseases': 'បញ្ជីជំងឺ',
        'tab_symptoms': 'បញ្ជីរោគសញ្ញា',
        'tab_rules': 'ច្បាប់វិនិច្ឆ័យ',
        'btn_add_disease': 'បន្ថែមជំងឺថ្មី',
        'btn_add_symptom': 'បន្ថែមរោគសញ្ញា',
        'btn_add_rule': 'បន្ថែមច្បាប់',
        'th_code': 'កូដ',
        'th_name': 'ឈ្មោះ',
        'th_scientific': 'ឈ្មោះវិទ្យាសាស្ត្រ',
        'th_severity': 'កម្រិតធ្ងន់ធ្ងរ',
        'th_category': 'ផ្នែករុក្ខជាតិ',
        'th_cf': 'កត្តាជឿជាក់ (CF)',
        'th_weight': 'ទម្ងន់',

        # Users Management
        'manage_users_title': 'គ្រប់គ្រងអ្នកប្រើប្រាស់',
        'manage_users_subtitle': 'ពិនិត្យ និងកែប្រែតួនាទីគណនីក្នុងប្រព័ន្ធ',
        'th_id': 'ល.រ',
        'btn_edit': 'កែប្រែ',
        'btn_delete': 'លុប',

        # Auth Pages
        'signin_title': 'ចូលប្រើប្រាស់',
        'signin_subtitle': 'ប្រព័ន្ធអ្នកជំនាញជំងឺដំណាំកាហ្វេ',
        'username_or_email_label': 'ឈ្មោះអ្នកប្រើប្រាស់ ឬ អ៊ីមែល',
        'password_label': 'ពាក្យសម្ងាត់',
        'remember_me_label': 'ចងចាំខ្ញុំក្នុងឧបករណ៍នេះ',
        'signin_submit_btn': 'ចូលគណនី',
        'no_account_text': 'មិនទាន់មានគណនី?',
        'register_link': 'ចុះឈ្មោះគណនីថ្មី',
        'demo_creds_title': 'គណនីគំរូសម្រាប់សាកល្បង (Demo Credentials):',
        'register_title': 'បង្កើតគណនីថ្មី',
        'register_subtitle': 'ចូលរួមប្រើប្រាស់ប្រព័ន្ធអ្នកជំនាញកាហ្វេ',
        'already_have_account': 'មានគណនីរួចហើយ?',
        'forgot_pw_title': 'ភ្លេចពាក្យសម្ងាត់',
        'forgot_pw_desc': 'បញ្ចូលអ៊ីមែលគណនីរបស់អ្នកដើម្បីទទួលបានតំណកំណត់ពាក្យសម្ងាត់ឡើងវិញ',
        'send_reset_link_btn': 'ផ្ញើតំណកំណត់ពាក្យសម្ងាត់',
        'back_to_login': 'ត្រឡប់ទៅទំព័រចូលគណនី',
    },

    'en': {
        # App Branding & Navigation
        'app_title': 'Coffee Disease Expert System',
        'app_brand': 'Coffee Expert System',
        'dashboard': 'Dashboard',
        'diagnose': 'Diagnose Disease',
        'cases_history': 'Case History',
        'rules_management': 'Rules Management',
        'users': 'Users',
        'my_profile': 'My Profile',
        'logout': 'Sign Out',
        'login': 'Sign In',
        'register': 'Register Account',
        'forgot_password': 'Forgot Password',
        'language': 'Language',
        'lang_km': 'ភាសាខ្មែរ',
        'lang_en': 'English',

        # Dashboard
        'hello': 'Hello',
        'welcome_subtitle_admin': 'Manage and monitor all diagnosis records, knowledge base rules, and user accounts system-wide.',
        'welcome_subtitle_user': 'Monitor your coffee crop health, inspect observed symptoms, and get timely treatments.',
        'admin_badge': 'Admin Console',
        'user_badge': 'Farmer / User',
        'new_diagnosis_btn': 'New Diagnosis',
        'total_cases_admin': 'Total System Cases',
        'total_cases_user': 'Total Diagnoses',
        'system_wide': 'System-wide',
        'personal_cases': 'Personal Cases',
        'month_cases_admin': 'Cases This Month (System)',
        'month_cases_user': 'Your Cases This Month',
        'current_month': 'Current Month',
        'avg_confidence': 'Avg Confidence',
        'knowledge_base': 'Knowledge Base',
        'diseases_unit': 'Diseases',
        'symptoms_unit': 'Symptoms',

        # Action Tiles
        'tile_diagnose_title': 'Diagnose Disease',
        'tile_diagnose_desc_admin': 'Execute inference with Forward Chaining',
        'tile_diagnose_desc_user': 'Select symptoms observed on your coffee plant',
        'tile_cases_title_admin': 'System Case History',
        'tile_cases_title_user': 'My Diagnosis History',
        'tile_cases_desc_admin': 'Inspect diagnosis cases of all users',
        'tile_cases_desc_user': 'Review past diagnoses and treatment advice',
        'tile_rules_title': 'Rules Management',
        'tile_rules_desc': 'Configure diseases, symptoms, and rule weights',
        'tile_users_title': 'User Management',
        'tile_users_desc': 'Manage accounts, roles, and system permissions',
        'tile_profile_title': 'My Profile',
        'tile_profile_desc': 'Update personal details and change password',

        # Tables & Lists
        'recent_cases_admin': 'Recent System Diagnoses',
        'recent_cases_user': 'Your Recent Diagnoses',
        'view_all': 'View All',
        'th_date': 'Date',
        'th_user': 'Farmer / User',
        'th_disease': 'Diagnosed Disease',
        'th_confidence': 'Certainty / Confidence',
        'th_location': 'Farm Location',
        'th_actions': 'Actions',
        'no_recent_cases': 'No diagnosis cases recorded yet',
        'start_first_diag': 'Start First Diagnosis',
        'view_details': 'View Details',
        'delete': 'Delete',
        'delete_confirm': 'Are you sure you want to delete this diagnosis record?',
        'unspecified': 'Not specified',
        'case_details_modal_title': 'Diagnosis Case Details',
        'treatment_label': 'Treatment:',
        'prevention_label': 'Prevention:',
        'notes_label': 'Notes:',
        'analysis_results_heading': 'Inference Results:',
        'no_detailed_results': 'No detailed results available',

        # Diagnosis Page
        'diag_header_title': 'Coffee Crop Disease Diagnosis',
        'diag_header_subtitle': 'Select all symptoms observed on your coffee plants for expert system inference',
        'all_categories': 'All Parts',
        'cat_leaf': 'Leaves',
        'cat_stem': 'Stems & Branches',
        'cat_root': 'Roots',
        'cat_fruit': 'Berries & Fruits',
        'search_symptoms_placeholder': 'Search symptoms (e.g. yellow spots, wilting, root rot...)',
        'selected_symptoms_badge': 'Selected',
        'clear_all': 'Clear All',
        'farm_location': 'Farm Location',
        'farm_location_placeholder': 'e.g. Mondulkiri, Ratanakiri, Pailin...',
        'farm_notes': 'Additional Observations',
        'farm_notes_placeholder': 'Plant age, watering schedule, weather conditions, or notes...',
        'submit_diagnosis_btn': 'Run Disease Diagnosis',
        'diag_result_title': 'Diagnosis Results',
        'no_disease_matched_title': 'No Specific Disease Matched',
        'no_disease_matched_desc': 'The selected symptoms did not match existing disease rules with sufficient confidence. Please select additional symptoms.',
        'run_new_diag': 'Diagnose Another Case',
        'diag_stepper_1': '1. Field Symptoms',
        'diag_stepper_2': '2. Farm Context',
        'diag_stepper_3': '3. Clinical Inference',
        'symptoms_catalog': 'Clinical Symptoms Catalog',
        'symptoms_catalog_sub': 'Select all symptoms matching your field observations',
        'select_all_btn': 'Select All',
        'deselect_all_btn': 'Deselect All',
        'selected_tray_title': 'Selected Symptoms',
        'selected_tray_empty': 'No symptoms selected yet. Click any symptom card on the left to select.',
        'quick_location_label': 'Quick Presets:',
        'sys_specs_title': 'System Specifications',
        'sys_specs_algo': 'Algorithm:',
        'sys_specs_algo_val': 'Forward Chaining + CF',
        'sys_specs_kb': 'Knowledge Base:',
        'sys_specs_kb_val': '15 Diseases & 17 Symptoms',
        'sys_specs_engine': 'Inference Engine:',
        'sys_specs_engine_val': 'Expert Rules Weighted Engine',
        'inspection_guide_title': 'Field Inspection Guide',
        'diff_diagnoses_title': 'Differential Diagnoses',
        'print_report_btn': 'Print Clinical Report',
        'save_history_btn': 'View in Cases History',

        # Cases History Page
        'cases_page_title': 'Diagnosis Cases History',
        'cases_page_subtitle': 'Review and audit all coffee disease diagnosis records saved in the system',
        'search_cases_placeholder': 'Search by disease name, location...',
        'period_all': 'All Time',
        'period_today': 'Today',
        'period_week': 'Last 7 Days',
        'period_month': 'Last 30 Days',
        'no_cases_period': 'No diagnosis records found for the selected time period',

        # Profile Page
        'profile_title': 'My Profile',
        'diagnoses_count_label': 'Diagnoses Made',
        'account_status_label': 'Account Status',
        'active_status': 'Active',
        'security_tips_title': 'Security Guidelines',
        'tip_length': 'Use a strong password with at least 6 characters.',
        'tip_share': 'Never share your account credentials with anyone.',
        'tip_change': 'Update your password periodically to keep your account safe.',
        'edit_account_title': 'Edit Profile Information',
        'username_label': 'Username',
        'username_cannot_change': 'Username cannot be modified',
        'role_label': 'Role',
        'role_admin_managed': 'Managed by system administrator',
        'full_name_label': 'Full Name',
        'email_label': 'Email Address',
        'save_changes_btn': 'Save Changes',
        'change_password_title': 'Change Password',
        'current_password_label': 'Current Password',
        'new_password_label': 'New Password',
        'confirm_password_label': 'Confirm New Password',
        'min_6_chars_placeholder': 'Minimum 6 characters',
        'update_password_btn': 'Update Password',

        # Rules Management
        'rules_title': 'Knowledge Base Management',
        'rules_subtitle': 'Configure diseases, symptoms, and Forward Chaining inference rules',
        'tab_diseases': 'Diseases',
        'tab_symptoms': 'Symptoms',
        'tab_rules': 'Diagnosis Rules',
        'btn_add_disease': 'Add Disease',
        'btn_add_symptom': 'Add Symptom',
        'btn_add_rule': 'Add Rule',
        'th_code': 'Code',
        'th_name': 'Name',
        'th_scientific': 'Scientific Name',
        'th_severity': 'Severity',
        'th_category': 'Plant Part',
        'th_cf': 'Certainty Factor (CF)',
        'th_weight': 'Weight',

        # Users Management
        'manage_users_title': 'User Management',
        'manage_users_subtitle': 'Review user accounts, update roles, and manage permissions',
        'th_id': 'ID',
        'btn_edit': 'Edit',
        'btn_delete': 'Delete',

        # Auth Pages
        'signin_title': 'Sign In',
        'signin_subtitle': 'Coffee Crop Disease Expert System',
        'username_or_email_label': 'Username or Email',
        'password_label': 'Password',
        'remember_me_label': 'Remember me on this device',
        'signin_submit_btn': 'Sign In to Account',
        'no_account_text': 'Don\'t have an account?',
        'register_link': 'Register New Account',
        'demo_creds_title': 'Demo Login Credentials:',
        'register_title': 'Create New Account',
        'register_subtitle': 'Join Coffee Disease Expert System',
        'already_have_account': 'Already have an account?',
        'forgot_pw_title': 'Forgot Password',
        'forgot_pw_desc': 'Enter your registered email address to receive password reset instructions',
        'send_reset_link_btn': 'Send Reset Link',
        'back_to_login': 'Back to Sign In',
    }
}

# English translations for Symptoms
SYMPTOM_TRANSLATIONS_EN = {
    'S01': {'name': 'Yellow spots on leaves', 'description': 'Small chlorotic yellow dots on leaf surface.'},
    'S02': {'name': 'Brown necrotic lesions', 'description': 'Brown dying spots appearing on foliage.'},
    'S03': {'name': 'Wilting, flaccid leaves', 'description': 'Leaves lose turgor and become soft and wilted.'},
    'S04': {'name': 'White powdery coating', 'description': 'Thin white talcum-like powdery layer on leaves.'},
    'S05': {'name': 'Premature leaf drop', 'description': 'Defoliation of green or infected leaves before season.'},
    'S06': {'name': 'Yellowing, drooping & wilting foliage', 'description': 'Coffee foliage turns yellow from base to tip, looking fatigued due to root decay or moisture deficiency.'},
    'S07': {'name': 'Black or brown decayed roots', 'description': 'Roots turn brown or black, becoming soggy and rotten.'},
    'S08': {'name': 'Curled, wavy & deformed leaves', 'description': 'Leaves curl inward, showing uneven wavy wrinkles or yellow-green mosaic discoloration.'},
    'S09': {'name': 'Concentric target rings on leaves', 'description': 'Distinct circular target-like necrotic rings centered on the foliage.'},
    'S10': {'name': 'Blackened dry twig dieback', 'description': 'Branch tips dry out, turn black, and die backward towards the main stem.'},
    'S11': {'name': 'Floury white powder over leaf surface', 'description': 'Thin flour-like fungal growth coating upper or lower leaf surfaces.'},
    'S12': {'name': 'Rusty orange velvety moss-like spots', 'description': 'Velvety raised orange or rusty red circular spots on leaves.'},
    'S13': {'name': 'Stem cracks with blackened inner wood', 'description': 'Cracks in the bark revealing dark brown or blackened vascular wood tissue.'},
    'S14': {'name': 'White fungal mycelial threads on twigs & leaves', 'description': 'Fine white fungal strands connecting branches and undersides of leaves.'},
    'S15': {'name': 'Collar rot & seedling collapse near ground', 'description': 'Stem near soil surface rots, softens, and causes young seedlings to collapse (damping off).'},
    'S16': {'name': 'Pinkish fungal crust on bark & branch forks', 'description': 'Pink or pale red crusty fungal layer growing on bark and branch crotches.'},
    'S17': {'name': 'Sooty black wipeable coating on leaves', 'description': 'Superficial black soot layer covering leaves that can be wiped or washed away.'}
}

# English translations for Diseases
DISEASE_TRANSLATIONS_EN = {
    'D01': {
        'name': 'Coffee Leaf Rust',
        'description': 'Fungal infection caused by Hemileia vastatrix affecting coffee foliage and reducing yield.',
        'treatment': 'Apply copper-based fungicides (e.g. Copper oxychloride) during early outbreak.',
        'prevention': 'Prune overcrowded shade branches to enhance air circulation and reduce dampness.'
    },
    'D02': {
        'name': 'Coffee Berry Disease',
        'description': 'Aggressive fungal disease causing dark sunken lesions on green coffee berries.',
        'treatment': 'Strip and destroy infected berries, apply targeted systemic fungicides.',
        'prevention': 'Regular farm hygiene inspections and timely fungicide spraying before rainy season.'
    },
    'D03': {
        'name': 'Brown Eye Spot (Cercospora Leaf Spot)',
        'description': 'Circular brown lesions with light grey centers surrounded by bright yellow halos.',
        'treatment': 'Apply Mancozeb, Azoxystrobin, or copper hydroxide according to recommended schedules.',
        'prevention': 'Prune dense canopies for sunlight penetration; balance soil nitrogen and potassium.'
    },
    'D04': {
        'name': 'Root Rot (Fusarium Wilt)',
        'description': 'Soil-borne fungal pathogen attacking root vascular systems causing severe wilting.',
        'treatment': 'Drench base with Metalaxyl or Carbendazim; excise rotting root sections.',
        'prevention': 'Ensure excellent plantation soil drainage; introduce beneficial Trichoderma bio-fungicides.'
    },
    'D05': {
        'name': 'Anthracnose Berry Spot',
        'description': 'Dark sunken necrotic spots on coffee berries causing premature fruit drop and mummification.',
        'treatment': 'Spray copper oxychloride or Chlorothalonil on developing berries and surrounding leaves.',
        'prevention': 'Harvest ripe berries promptly; dispose of mummified fruit away from the plantation.'
    },
    'D06': {
        'name': 'Coffee Leaf Curl Virus',
        'description': 'Viral pathogen causing severe leaf puckering, stunted growth, and distorted canopy.',
        'treatment': 'No curative treatment exists; control insect vectors (aphids, thrips) and rogue out diseased plants.',
        'prevention': 'Plant disease-resistant certified seedlings and maintain strict pest control.'
    },
    'D07': {
        'name': 'Target Leaf Spot',
        'description': 'Large necrotic leaf lesions displaying concentric rings resembling shooting targets.',
        'treatment': 'Apply Pyraclostrobin or Chlorothalonil fungicides to infected canopy.',
        'prevention': 'Maintain wide plant spacing and prune lower branches close to the ground.'
    },
    'D08': {
        'name': 'Bacterial Blight / Twig Dieback',
        'description': 'Bacterial infection triggering blackened twig necrosis and retrograde shoot dieback.',
        'treatment': 'Prune affected shoots 5-10 cm below damaged margin; spray copper-based bactericides.',
        'prevention': 'Prevent mechanical wounding during pruning/harvest; avoid excessive nitrogen.'
    },
    'D09': {
        'name': 'Powdery Mildew',
        'description': 'Superficial whitish fungal powdery growth impairing photosynthesis on leaf surfaces.',
        'treatment': 'Spray sulfur-based formulations or Difenoconazole at the first sign of mildew.',
        'prevention': 'Thin dense shade trees to allow sun penetration and boost airflow.'
    },
    'D10': {
        'name': 'Algal Leaf Spot (Red Rust)',
        'description': 'Parasitic green/orange algae forming raised velvety spots on shaded coffee leaves.',
        'treatment': 'Apply copper oxychloride sprays to eliminate algal colonies.',
        'prevention': 'Improve drainage and open up the canopy to let sunlight reach the lower branches.'
    },
    'D11': {
        'name': 'Coffee Wilt Disease (Tracheomycosis)',
        'description': 'Fatal vascular wilt disease causing rapid defoliation and blackened internal stem tissues.',
        'treatment': 'Incurable; immediately uproot, burn infected coffee trees, and quarantine the area.',
        'prevention': 'Disinfect pruning tools and use resistant varieties (especially in Robusta fields).'
    },
    'D12': {
        'name': 'Thread Blight (Black Rot)',
        'description': 'White fungal mycelial strands binding dead dry leaves onto branches so they hang without falling.',
        'treatment': 'Spray Validamycin or Copper hydroxide thoroughly over affected stems and twigs.',
        'prevention': 'Reduce plant density and avoid dark damp microclimates within the coffee plot.'
    },
    'D13': {
        'name': 'Damping-off of Seedlings',
        'description': 'Rotting of the seedling collar near ground level causing sudden collapse in nursery beds.',
        'treatment': 'Drench nursery soil with Mancozeb or Carbendazim at first sign of damping off.',
        'prevention': 'Use pasteurized nursery media, avoid waterlogging, and space nursery seedlings properly.'
    },
    'D14': {
        'name': 'Pink Disease',
        'description': 'Pinkish crust-like fungal growth across branches and forks causing bark cracking and limb death.',
        'treatment': 'Scrape away fungal crust and paint infected wounds with copper or Tridemorph paste.',
        'prevention': 'Prune dead wood before the rainy season and prune to keep plantation humidity low.'
    },
    'D15': {
        'name': 'Sooty Mold',
        'description': 'Black superficial fungal layer feeding on honeydew secreted by sap-sucking insects.',
        'treatment': 'Wash foliage with mild agricultural soap/mineral oil; spray insecticide against aphids and scale.',
        'prevention': 'Control mealybugs, aphids, and ants that tend honeydew-producing pests.'
    }
}


def gettext(key, lang='km', default=None):
    """Retrieve translated string for given key and language (defaults to Khmer)."""
    lang_dict = TRANSLATIONS.get(lang) or TRANSLATIONS['km']
    val = lang_dict.get(key)
    if val is not None:
        return val
    # Fallback to Khmer
    fallback = TRANSLATIONS['km'].get(key)
    if fallback is not None:
        return fallback
    return default or key


def get_localized_symptom(symptom, lang='km'):
    """Return dict or object with localized name and description for Symptom."""
    if not symptom:
        return None
    code = getattr(symptom, 'code', None) or (symptom.get('code') if isinstance(symptom, dict) else None)
    default_name = getattr(symptom, 'name', None) or (symptom.get('name') if isinstance(symptom, dict) else '')
    default_desc = getattr(symptom, 'description', None) or (symptom.get('description') if isinstance(symptom, dict) else '')
    
    if lang == 'en' and code in SYMPTOM_TRANSLATIONS_EN:
        en_data = SYMPTOM_TRANSLATIONS_EN[code]
        return {
            'name': en_data['name'],
            'description': en_data['description'] or default_desc
        }
    return {
        'name': default_name,
        'description': default_desc
    }


def get_localized_disease(disease, lang='km'):
    """Return dict with localized name, description, treatment, and prevention for Disease."""
    if not disease:
        return None
    code = getattr(disease, 'code', None) or (disease.get('code') if isinstance(disease, dict) else None)
    default_name = getattr(disease, 'name', None) or (disease.get('name') if isinstance(disease, dict) else '')
    default_desc = getattr(disease, 'description', None) or (disease.get('description') if isinstance(disease, dict) else '')
    default_treat = getattr(disease, 'treatment', None) or (disease.get('treatment') if isinstance(disease, dict) else '')
    default_prev = getattr(disease, 'prevention', None) or (disease.get('prevention') if isinstance(disease, dict) else '')
    
    if lang == 'en' and code in DISEASE_TRANSLATIONS_EN:
        en_data = DISEASE_TRANSLATIONS_EN[code]
        return {
            'name': en_data['name'],
            'description': en_data['description'] or default_desc,
            'treatment': en_data['treatment'] or default_treat,
            'prevention': en_data['prevention'] or default_prev
        }
    return {
        'name': default_name,
        'description': default_desc,
        'treatment': default_treat,
        'prevention': default_prev
    }

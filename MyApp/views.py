import types ,os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import job_seeker , job_provider , company ,users ,contact_us, job_details ,viewApplicants ,viewApplicants_1

def home(request):
    return render(request,'home_1.html')

def JS(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        m_name = request.POST['m_name']
        gender = request.POST['gender']
        uid_type = request.POST['uid_type']
        uid_number = request.POST['uid_number']
        dob = request.POST['dob']
        state = request.POST['state']
        pincode = request.POST['pincode']
        city = request.POST['city']
        add = request.POST['add']
        email_id = request.POST['email_id']
        mobile_no = request.POST['mobile_no']
        pwd = request.POST['pwd']
        u_name = request.POST['u_name']
        js_security_question = request.POST['js_security_question']
        js_ans_security_question = request.POST['js_ans_security_question']
        js_profile_pic = request.FILES.get('js_profile_pic','profile.png')
        print(js_profile_pic)
        if js_profile_pic != 'profile.png':
            path = 'static/User_profile/'
            format_ = os.path.join(path, u_name)
            img_extension = os.path.splitext(js_profile_pic.name)[1]
            img_save_path = format_ + img_extension
            with open(img_save_path, 'wb+') as f:
                for chunk in js_profile_pic.chunks():
                    f.write(chunk)
        else:
            
            img_save_path = 'static/User_profile/profile.png'

        storeInTable = job_seeker(f_name=f_name,l_name=l_name,m_name=m_name,gender=gender,uid_type=uid_type,uid_number=uid_number,dob=dob,state=state,email_id=email_id,mobile_no=mobile_no,pwd=pwd,u_name=u_name,pincode=pincode,city=city,add=add,js_security_question=js_security_question,js_ans_security_question=js_ans_security_question,js_profile_pic=img_save_path)
        storeInTable.save()
        storeInTable3=users(user_type='JS',u_name=u_name,pwd=pwd)
        storeInTable3.save()
        print('User Created')
        return redirect('login')      
        
    else:
        return render(request,'jobseeker.html')

def JP(request):
    if request.method == 'POST':
        company_id = request.POST['company_id']
        company_name = request.POST['company_name']
        company_type = request.POST['company_type']
        company_state = request.POST['company_state']
        company_city = request.POST['company_city']
        company_add = request.POST['company_add']
        company_pincode = request.POST['company_pincode']
        company_mobile_no = request.POST['company_mobile_no']
        company_email_id = request.POST['company_email_id']
        company_url = request.POST['company_url']
        
        company_logo = request.FILES.get('company_logo','symbol.png')
        print(company_logo)
        if company_logo != 'symbol.PNG':
            path = 'static/Company_Logo/'
            format_ = os.path.join(path, company_id)
            img_extension = os.path.splitext(company_logo.name)[1]
            img_save_path = format_ + img_extension
            with open(img_save_path, 'wb+') as f:
                for chunk in company_logo.chunks():
                    f.write(chunk)
        else:
            
            img_save_path = 'static/Company_Logo/symbol.png'
            

        job_provider_company_id = request.POST['company_id']
        job_provider_fname = request.POST['job_provider_fname']
        job_provider_mname = request.POST['job_provider_mname']
        job_provider_lname = request.POST['job_provider_lname']
        job_provider_gender = request.POST['job_provider_gender']
        job_provider_position = request.POST['job_provider_position']
        u_name = request.POST['u_name']
        pwd = request.POST['pwd']
        jp_security_question = request.POST['jp_security_question']
        jp_ans_security_question = request.POST['jp_ans_security_question']

        if job_provider.objects.filter(u_name = u_name).exists():
            print(company_name)
            messages.info(request,'UserName Already Exists')
            return render(request,'jobprovider.html',{'company_id':company_id,'company_name':company_name,'company_type':company_type,'company_state':company_state,'company_city':company_city,'company_add':company_add,'company_pincode':company_pincode,'company_mobile_no':company_mobile_no,'company_email_id':company_email_id,'company_url':company_url,'job_provider_fname':job_provider_fname,'job_provider_mname':job_provider_mname,'job_provider_lname':job_provider_lname,'job_provider_gender':job_provider_gender,'job_provider_position':job_provider_position,'jp_security_question':jp_security_question,'jp_ans_security_question':jp_ans_security_question})
        else:
            storeInTable1 = company(company_id=company_id,company_name=company_name,company_type=company_type,company_state=company_state,company_city=company_city,company_add=company_add,company_pincode=company_pincode,company_mobile_no=company_mobile_no,company_email_id=company_email_id,company_url=company_url,company_logo=img_save_path)
            storeInTable1.save()
            storeInTable2 = job_provider(job_provider_company_id=company_id,job_provider_fname=job_provider_fname,job_provider_mname=job_provider_mname,job_provider_lname=job_provider_lname,job_provider_gender=job_provider_gender,job_provider_position=job_provider_position,u_name=u_name,pwd=pwd,jp_security_question=jp_security_question,jp_ans_security_question=jp_ans_security_question)
            storeInTable2.save()
            storeInTable3=users(user_type='JP',u_name=u_name,pwd=pwd)
            storeInTable3.save()
            
            print('User Created')
            return redirect('login')
    else:
        return render(request,'jobprovider.html')

def login(request):
    if request.method == 'POST':
        u_name = request.POST['u_name'] 
        pwd = request.POST['pwd']
        user_type = request.POST['user_type']
        
        if users.objects.filter(u_name = u_name ,pwd=pwd , user_type="JS").exists():
            user_det = job_seeker.objects.all().values('js_profile_pic').get(u_name = u_name)

            if job_details.objects.exists():
                Job_Det = job_details.objects.all().values('jd_job_id','jd_category','jd_company_id','jd_company_name','jd_location','jd_position','jd_salary','jd_start_date','jd_apply_by','jd_posted_on','jd_duration','jd_skills_required','jd_perks','jd_vacancy','jd_experience','jd_description')
                
                ID = job_details.objects.all().values('jd_company_id')
                n= ID.count()
                
                profile =[]
                x = []
                for id_ ,i in zip(ID,range(n)):
                    profile.append(company.objects.all().values('company_logo').filter(company_id=id_['jd_company_id']))
                    x.append(profile[i][0]['company_logo'])
                return render(request,'js_hpage.html',{'path':zip(Job_Det,x,range(n)),'u_name':u_name,'user_det':user_det['js_profile_pic']})
            else:
                Job_Det = "No Applications Yet!!"
                return render(request,'js_hpage.html',{'u_name':u_name,'user_det':user_det['js_profile_pic']})
            
        elif users.objects.filter(u_name = u_name ,pwd=pwd , user_type="JP").exists():

            company_id = job_provider.objects.all().values('job_provider_company_id').get(u_name = u_name)
            profile = company.objects.all().values('company_logo','company_name','company_id').get(company_id=company_id['job_provider_company_id'])
            #flag = viewApplicants.objects.all().values('va_status').get(va_u_name=u_name,va_company_name=profile['company_name'])
            flag = ""
            if job_details.objects.exists():
                Job_Det = job_details.objects.all().values('jd_job_id','jd_category','jd_company_name','jd_location','jd_position','jd_salary','jd_start_date','jd_apply_by','jd_posted_on','jd_duration').filter(jd_company_id=company_id['job_provider_company_id'],jd_company_name=profile['company_name'])
                
            else:
                Job_Det = "No Applications Yet!!"
                
            return render(request,'jp_hpage.html',{'company_name':profile['company_name'],'flag':flag,'u_name':u_name,'path':profile['company_logo'],'company_id':profile['company_id'],'Job_Det':Job_Det})
        else:
            messages.info(request,' *Enter Valid Username or Password')
            return redirect('login')
   

    else:
        return render(request,'login_page.html')

def AS(request):
    return render(request, 'about_us.html')

def CS(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        subject = request.POST['subject']
        storeInTable = contact_us(f_name=fname,l_name=lname,query=subject)
        storeInTable.save()
        msg = "Sent your Response!!"
        return render(request,'contact_us.html',{'msg':msg})
    else:
        msg = "Have a query? Just leave us a message:"
        return render(request,'contact_us.html',{'msg':msg})

def uname(request):
    
    return render(request,'username.html')

def resetpwd(request):
    if request.method == 'POST':
        u_name = request.POST['u_name']
        if users.objects.filter(u_name = u_name).exists():
            u_type = users.objects.all().values('user_type').get(u_name = u_name)
            
            if u_type['user_type'] == "JS":
                js_ans_security_question = request.POST['ans']
                check = job_seeker.objects.all().values('js_security_question','js_ans_security_question').get(u_name=u_name)
                
                security_question = check['js_security_question']
                if check['js_ans_security_question']== js_ans_security_question:
                    return render(request,'reset_password.html',{'u_name':u_name})
                else:
                    messages.info(request,'*Enter Correct Answer')
                    return render(request,'forgot_pwd.html',{'security_question':security_question,'u_name':u_name})

            elif u_type['user_type'] == "JP":
                jp_ans_security_question = request.POST['ans']
                check = job_provider.objects.all().values('jp_security_question','jp_ans_security_question').get(u_name=u_name)
                
                security_question = check['jp_security_question']
                if check['jp_ans_security_question']== jp_ans_security_question:
                    return render(request,'reset_password.html',{'u_name':u_name})
                else:
                    messages.info(request,'*Enter Correct Answer')
                    return render(request,'forgot_pwd.html',{'security_question':security_question,'u_name':u_name})
    else:
        return render(request, 'reset_password.html')

def forgotpwd(request):
    if request.method == 'POST':
        u_name = request.POST['u_name']

        if users.objects.filter(u_name = u_name).exists():
            u_type = users.objects.all().values('user_type').get(u_name = u_name)

            if u_type['user_type'] == "JS":
                security_que = job_seeker.objects.all().values('js_security_question').get(u_name = u_name)
                security_question = security_que['js_security_question']
            elif u_type['user_type'] == "JP":
                security_que = job_provider.objects.all().values('jp_security_question').get(u_name = u_name)
                security_question = security_que['jp_security_question']
            return render(request,'forgot_pwd.html',{'security_question':security_question,'u_name':u_name})
        else:
            messages.info(request,'*Enter Valid Username')
            return redirect('username')
        
    
def SavePass(request):
    print('hi')
    if request.method == 'POST':
        u_name = request.POST['u_name']
        
        print(u_name)
        u_type = users.objects.all().values('user_type').get(u_name = u_name)
        if u_type['user_type'] == "JS":
            print('JS')
            U = users.objects.all().values('user_type','u_name','pwd').get(u_name = u_name)
            JSF = job_seeker.objects.all().values('f_name','m_name','l_name','gender','uid_type','uid_number','u_name','dob','state','city','add','pincode','email_id','mobile_no','pwd','js_security_question','js_ans_security_question','js_profile_pic').get(u_name = u_name)
            pwd = request.POST['pwd']
            storeInTable1 = job_seeker(f_name=JSF['f_name'],l_name=JSF['l_name'],m_name=JSF['m_name'],gender=JSF['gender'],uid_type=JSF['uid_type'],uid_number=JSF['uid_number'],dob=JSF['dob'],state=JSF['state'],email_id=JSF['email_id'],mobile_no=JSF['mobile_no'],pwd=pwd,u_name=u_name,pincode=JSF['pincode'],city=JSF['city'],add=JSF['add'],js_security_question=JSF['js_security_question'],js_ans_security_question=JSF['js_ans_security_question'],js_profile_pic=JSF['js_profile_pic'])
            storeInTable1.save()
            storeInTable2 = users(user_type=U['user_type'],u_name=u_name,pwd=pwd)
            storeInTable2.save()
        elif u_type['user_type'] == "JP":
            print('JP')
            JPF = job_provider.objects.all().values('job_provider_company','job_provider_fname','job_provider_mname','job_provider_lname','job_provider_gender','job_provider_position','u_name','pwd','jp_security_question','jp_ans_security_question').get(u_name = u_name)
            pwd = request.POST['pwd']
            storeInTable1 = job_provider(job_provider_company_id=JSF['job_provider_company_id'],job_provider_fname=JSF['job_provider_fname'],job_provider_mname=JSF['job_provider_mname'],job_provider_lname=JSF['job_provider_lname'],job_provider_gender=JSF['job_provider_gender'],job_provider_position=JSF['job_provider_position'],u_name=JSF['u_name'],pwd=JSF['pwd'],jp_security_question=JSF['jp_security_question'],jp_ans_security_question=JSF['jp_ans_security_question'])
            storeInTable1.save()
            storeInTable2 = users(user_type=U['user_type'],u_name=u_name,pwd=pwd)
            storeInTable2.save()
        return redirect('login')

def updateJS(request):
    if request.method == 'POST':
        u_name = request.POST['u_name']
        user_det = request.POST['user_det']
        JS = job_seeker.objects.all().values('f_name','m_name','l_name','gender','uid_type','uid_number','dob','state','city','add','pincode','email_id','mobile_no','pwd','u_name','js_security_question','js_ans_security_question','js_profile_pic').get(u_name=u_name)
        x = str(JS['dob'])
        print(user_det)
    return render(request, 'updatePageJS.html',{'JS':JS,'x':x,'user_det':user_det})

def UPJS(request):
    if request.method == 'POST':
        reset =  request.POST['reset']
        user_det = request.POST['user_det']
        if reset == "reset":
            u_name = request.POST['u_name']
            #user_det = request.POST['user_det']
            JS = job_seeker.objects.all().values('f_name','m_name','l_name','gender','uid_type','uid_number','dob','state','city','add','pincode','email_id','mobile_no','pwd','u_name','js_security_question','js_ans_security_question','js_profile_pic').get(u_name=u_name)
            x = str(JS['dob'])
            print(type(x),x)
            return render(request, 'updatePageJS.html',{'JS':JS,'x':x,'user_det':user_det})
        elif reset == "delete":
            u_name = request.POST['u_name']
            job_seeker.objects.get(u_name=u_name).delete()
            users.objects.get(u_name=u_name).delete()
            viewApplicants.objects.filter(va_u_name=u_name).delete()
            viewApplicants_1.objects.filter(va_u_name=u_name).delete()
            return redirect('/')
        else:
            f_name = request.POST['f_name']
            l_name = request.POST['l_name']
            m_name = request.POST['m_name']
            gender = request.POST['gender']
            uid_type = request.POST['uid_type']
            uid_number = request.POST['uid_number']
            dob = request.POST['dob']
            state = request.POST['state']
            pincode = request.POST['pincode']
            city = request.POST['city']
            add = request.POST['add']
            email_id = request.POST['email_id']
            mobile_no = request.POST['mobile_no']
            pwd = request.POST['pwd']
            u_name = request.POST['u_name']
            js_security_question = request.POST['js_security_question']
            js_ans_security_question = request.POST['js_ans_security_question']
            print(user_det)
            storeInTable = job_seeker(f_name=f_name,l_name=l_name,m_name=m_name,gender=gender,uid_type=uid_type,uid_number=uid_number,dob=dob,state=state,email_id=email_id,mobile_no=mobile_no,pwd=pwd,u_name=u_name,pincode=pincode,city=city,add=add,js_security_question=js_security_question,js_ans_security_question=js_ans_security_question,js_profile_pic=user_det)
            storeInTable.save()
            storeInTable3=users(user_type='JS',u_name=u_name,pwd=pwd)
            storeInTable3.save()
            return HJS(request,u_name,user_det)

def UPJP(request):
    if request.method == 'POST':
        reset =  request.POST['reset']
        path = request.POST['path']
        u_name = request.POST['u_name']
        flag = request.POST['flag']
        if reset == "reset":
            company_id = request.POST['company_id']
            CP = company.objects.all().values('company_id','company_name','company_type','company_state','company_city','company_add','company_pincode','company_mobile_no','company_email_id','company_url').get(company_id=company_id)
            JP = job_provider.objects.all().values('job_provider_fname','job_provider_mname','job_provider_lname','job_provider_gender','job_provider_position','u_name','pwd','jp_security_question','jp_ans_security_question').get(job_provider_company_id=company_id)    
            return render(request,'updatePageJP.html',{'CP':CP,'JP':JP,'flag':flag,'company_id':company_id,'path':path,'cname':CP['company_type'],'sq':JP['jp_security_question']})
        elif reset == "delete":
            company_id = request.POST['company_id']
            CP = company.objects.all().values('company_name').get(company_id=company_id)
            job_provider.objects.get(job_provider_company_id=company_id).delete()
            users.objects.get(u_name=u_name).delete()
            company.objects.get(company_id=company_id).delete()
            job_details.objects.filter(jd_company_id=company_id).delete()
            
            viewApplicants.objects.filter(va_company_name=CP['company_name']).delete()
            viewApplicants_1.objects.filter(va_company_name=CP['company_name']).delete()
            return redirect('/')
        else:
            company_id = request.POST['company_id']
            company_name = request.POST['company_name']
            company_type = request.POST['company_type']
            company_state = request.POST['company_state']
            company_city = request.POST['company_city']
            company_add = request.POST['company_add']
            company_pincode = request.POST['company_pincode']
            company_mobile_no = request.POST['company_mobile_no']
            company_email_id = request.POST['company_email_id']
            company_url = request.POST['company_url']
            job_provider_company_id = request.POST['company_id']
            job_provider_fname = request.POST['job_provider_fname']
            job_provider_mname = request.POST['job_provider_mname']
            job_provider_lname = request.POST['job_provider_lname']
            job_provider_gender = request.POST['job_provider_gender']
            job_provider_position = request.POST['job_provider_position']
            u_name = request.POST['u_name']
            pwd = request.POST['pwd']
            jp_security_question = request.POST['jp_security_question']
            jp_ans_security_question = request.POST['jp_ans_security_question']

            
            storeInTable1 = company(company_id=company_id,company_name=company_name,company_type=company_type,company_state=company_state,company_city=company_city,company_add=company_add,company_pincode=company_pincode,company_mobile_no=company_mobile_no,company_email_id=company_email_id,company_url=company_url,company_logo=path)
            storeInTable1.save()
            storeInTable2 = job_provider(job_provider_company_id=company_id,job_provider_fname=job_provider_fname,job_provider_mname=job_provider_mname,job_provider_lname=job_provider_lname,job_provider_gender=job_provider_gender,job_provider_position=job_provider_position,u_name=u_name,pwd=pwd,jp_security_question=jp_security_question,jp_ans_security_question=jp_ans_security_question)
            storeInTable2.save()
            storeInTable3=users(user_type='JP',u_name=u_name,pwd=pwd)
            storeInTable3.save()

            company_id_ = job_provider.objects.all().values('job_provider_company_id').get(job_provider_company_id = company_id)
            profile = company.objects.all().values('company_logo','company_name','company_id').get(company_id=company_id_['job_provider_company_id'])
            Job_Det = job_details.objects.all().values('jd_job_id','jd_category','jd_company_name','jd_location','jd_position','jd_salary','jd_start_date','jd_apply_by','jd_posted_on','jd_duration').filter(jd_company_id=company_id_['job_provider_company_id'],jd_company_name=profile['company_name'])

            return render(request,'jp_hpage.html',{'company_name':profile['company_name'],'flag':flag,'u_name':u_name,'path':profile['company_logo'],'company_id':profile['company_id'],'Job_Det':Job_Det})
def updateJP(request):
    if request.method == 'POST':
        company_id = request.POST['company_id']
        path = request.POST['path']
        u_name = request.POST['u_name']
        flag = request.POST['flag']
        CP = company.objects.all().values('company_id','company_name','company_type','company_state','company_city','company_add','company_pincode','company_mobile_no','company_email_id','company_url').get(company_id=company_id)
        JP = job_provider.objects.all().values('job_provider_fname','job_provider_mname','job_provider_lname','job_provider_gender','job_provider_position','u_name','pwd','jp_security_question','jp_ans_security_question').get(job_provider_company_id=company_id)    
        print(JP['job_provider_gender'],CP['company_type'],JP['jp_security_question'])
    return render(request,'updatePageJP.html',{'CP':CP,'JP':JP,'flag':flag,'company_id':company_id,'path':path,'cname':CP['company_type'],'sq':JP['jp_security_question']})

def AddJob(request):
    if request.method == 'POST':
        
        company_name = request.POST['company_name']
        company_id = request.POST['company_id']
        u_name = request.POST['u_name']
        print(company_name,company_id)
        profile = company.objects.all().values('company_logo','company_name','company_id').get(company_id=company_id)

        
        return render(request,'Job_Details.html',{'company_name':company_name,'path':profile['company_logo'],'company_id':company_id,'u_name':u_name})
    else:
        return render(request,'Job_Details.html')

def JD(request):
    if request.method == 'POST':
        jd_company_id = request.POST['company_id']
        jd_company_name = request.POST['company_name']
        jd_job_id = request.POST['jd_job_id']
        jd_position = request.POST['jd_position']
        jd_location = request.POST['jd_location']
        jd_skills_required = request.POST['jd_skills_required']
        jd_category = request.POST['jd_category']
        jd_salary = request.POST['jd_salary']
        jd_vacancy =request.POST['jd_vacancy']
        jd_experience =request.POST['jd_experience']
        jd_description =request.POST['jd_description']
        jd_start_date = request.POST['jd_start_date']
        jd_apply_by = request.POST['jd_apply_by']
        jd_posted_on = request.POST['jd_posted_on']
        jd_duration = request.POST['jd_duration']
        jd_perks = request.POST['jd_perks']
        u_name = request.POST['u_name']
        storeInTable1 = job_details(jd_company_id=jd_company_id,jd_company_name=jd_company_name,jd_job_id=jd_job_id,jd_position=jd_position,jd_location=jd_location,jd_skills_required=jd_skills_required,jd_category=jd_category,jd_salary=jd_salary,jd_vacancy=jd_vacancy,jd_experience=jd_experience,jd_description=jd_description,jd_start_date=jd_start_date,jd_apply_by=jd_apply_by,jd_posted_on=jd_posted_on,jd_duration=jd_duration,jd_perks=jd_perks)
        storeInTable1.save()
        company_id = job_provider.objects.all().values('job_provider_company_id').get(job_provider_company_id = jd_company_id)
        profile = company.objects.all().values('company_logo','company_name','company_id').get(company_id=company_id['job_provider_company_id'])
        
        if job_details.objects.exists():
            Job_Det = job_details.objects.all().values('jd_job_id','jd_category','jd_company_name','jd_location','jd_position','jd_salary','jd_start_date','jd_apply_by','jd_posted_on','jd_duration').filter(jd_company_id=company_id['job_provider_company_id'],jd_company_name=profile['company_name'])
                
        else:
            Job_Det = "No Applications Yet!!"
                
        return render(request,'jp_hpage.html',{'company_name':profile['company_name'],'path':profile['company_logo'],'company_id':profile['company_id'],'Job_Det':Job_Det,'u_name':u_name})
      
    else:

        return render(request,'Job_Details.html')

def FilterJob(request):
    if request.method == 'POST':
        position = request.POST['filter_pos']
        location = request.POST['filter_loc']
        category = request.POST['filter_cat']
        u_name = request.POST['u_name']
        user_det = request.POST['user_det']
        print(u_name,user_det)
        user_det = job_seeker.objects.all().values('js_profile_pic').get(u_name = u_name)
        if  position != "Select Position" and  location != "":
            print('In 1')
            
            Job_Det = job_details.objects.all().values('jd_job_id','jd_category','jd_company_id','jd_company_name','jd_location','jd_position','jd_salary','jd_start_date','jd_apply_by','jd_posted_on','jd_duration','jd_skills_required','jd_perks','jd_vacancy','jd_experience','jd_description').filter(jd_position=position,jd_category=category,jd_location=location)
            ID = job_details.objects.all().values('jd_company_id').filter(jd_position=position,jd_category=category,jd_location=location)
            n= ID.count()
            
            profile =[]
            x = []
            for id_ ,i in zip(ID,range(n)):
                profile.append(company.objects.all().values('company_logo').filter(company_id=id_['jd_company_id']))
                x.append(profile[i][0]['company_logo'])
            
        elif position == "Select Position" and location != "":
            print('In 2')
            Job_Det = job_details.objects.all().values('jd_job_id','jd_category','jd_company_id','jd_company_name','jd_location','jd_position','jd_salary','jd_start_date','jd_apply_by','jd_posted_on','jd_duration','jd_skills_required','jd_perks','jd_vacancy','jd_experience','jd_description').filter(jd_category=category,jd_location=location)
            ID = job_details.objects.all().values('jd_company_id').filter(jd_category=category,jd_location=location)
            n= ID.count()
            print(Job_Det)
            profile =[]
            x = []
            for id_ ,i in zip(ID,range(n)):
                profile.append(company.objects.all().values('company_logo').filter(company_id=id_['jd_company_id']))
                x.append(profile[i][0]['company_logo'])
            
        elif position != "Select Position" and location == "":
            print('In 3')
            Job_Det = job_details.objects.all().values('jd_job_id','jd_category','jd_company_id','jd_company_name','jd_location','jd_position','jd_salary','jd_start_date','jd_apply_by','jd_posted_on','jd_duration','jd_skills_required','jd_perks','jd_vacancy','jd_experience','jd_description').filter(jd_category=category,jd_position=position)
            ID = job_details.objects.all().values('jd_company_id').filter(jd_category=category,jd_position=position)
            n= ID.count()
            print(Job_Det)
            profile =[]
            x = []
            for id_ ,i in zip(ID,range(n)):
                profile.append(company.objects.all().values('company_logo').filter(company_id=id_['jd_company_id']))
                x.append(profile[i][0]['company_logo'])
            
        else:
            print('In 4')
            Job_Det = job_details.objects.all().values('jd_category','jd_job_id','jd_company_id','jd_company_name','jd_location','jd_position','jd_salary','jd_start_date','jd_apply_by','jd_posted_on','jd_duration','jd_skills_required','jd_perks','jd_vacancy','jd_experience','jd_description').filter(jd_category=category)
            ID = job_details.objects.all().values('jd_company_id').filter(jd_category=category)
            n= ID.count()
            
            profile =[]
            x = []
            for id_ ,i in zip(ID,range(n)):
                profile.append(company.objects.all().values('company_logo').filter(company_id=id_['jd_company_id']))
                x.append(profile[i][0]['company_logo'])
        if len(x) == 0:
            return render(request,'js_hpage.html',{'path':zip(Job_Det,x,range(n)),'u_name':u_name,'user_det':user_det['js_profile_pic']})
        else:
            return render(request,'js_hpage.html',{'path':zip(Job_Det,x,range(n)),'u_name':u_name,'user_det':user_det['js_profile_pic']})
        #return render(request,'js_hpage.html')

def HJS(request,u_name,user_det):
    profile =[]
    x = []
    n=0
    if job_details.objects.exists():
        Job_Det = job_details.objects.all().values('jd_category','jd_job_id','jd_company_id','jd_company_name','jd_location','jd_position','jd_salary','jd_start_date','jd_apply_by','jd_posted_on','jd_duration','jd_skills_required','jd_perks','jd_vacancy','jd_experience','jd_description')
                
        ID = job_details.objects.all().values('jd_company_id')
        n= ID.count()
                
        
        for id_ ,i in zip(ID,range(n)):
            profile.append(company.objects.all().values('company_logo').filter(company_id=id_['jd_company_id']))
            x.append(profile[i][0]['company_logo'])
                
    else:
        Job_Det = "No Applications Yet!!"
            
    return render(request,'js_hpage.html',{'path':zip(Job_Det,x,range(n)),'u_name':u_name,'user_det':user_det})
    
def HJS_(request):
    if request.method == 'POST':
        u_name = request.POST['u_name']
        user_det = request.POST['user_det']
        if job_details.objects.exists():
            Job_Det = job_details.objects.all().values('jd_category','jd_job_id','jd_company_id','jd_company_name','jd_location','jd_position','jd_salary','jd_start_date','jd_apply_by','jd_posted_on','jd_duration','jd_skills_required','jd_perks','jd_vacancy','jd_experience','jd_description')
                    
            ID = job_details.objects.all().values('jd_company_id')
            n= ID.count()
            print(ID)
            profile =[]
            x = []
            for id_ ,i in zip(ID,range(n)):
                profile.append(company.objects.all().values('company_logo').filter(company_id=id_['jd_company_id']))
                x.append(profile[i][0]['company_logo'])
                
            return render(request,'js_hpage.html',{'path':zip(Job_Det,x,range(n)),'u_name':u_name,'user_det':user_det})   
        else:
            print('i')
            Job_Det = "No Applications Yet!!"
            return render(request,'js_hpage.html',{'u_name':u_name,'user_det':user_det})
    
def HJP(request):
    if request.method == 'POST':
        company_id = request.POST['company_id']
        path = request.POST['path']
        u_name = request.POST['u_name']
        flag = request.POST['flag']
        #company_id = job_provider.objects.all().values('job_provider_company_id').get(u_name = u_name)
        profile = company.objects.all().values('company_logo','company_name').get(company_id=company_id)
                
        if job_details.objects.exists():
            Job_Det = job_details.objects.all().values('jd_job_id','jd_category','jd_company_name','jd_location','jd_position','jd_salary','jd_start_date','jd_apply_by','jd_posted_on','jd_duration').filter(jd_company_id=company_id,jd_company_name=profile['company_name'])
        else:
            Job_Det = "No Applications Yet!!"
        return render(request,'jp_hpage.html',{'company_name':profile['company_name'],'flag':flag,'u_name':u_name,'path':path,'company_id':company_id,'Job_Det':Job_Det})
    #return render(request,'jp_hpage.html')

def VAC(request):
  
    if request.method == 'POST':
        path = request.POST['path']
        company_name = request.POST['company_name']
        job_id = request.POST['job_id']
        company_id = request.POST['company_id']
        u_name = request.POST['u_name']
        #flag = request.POST['flag']
        User_Det = viewApplicants_1.objects.all().values('va_u_name','va_resume','va_status').filter(va_job_id=job_id,va_company_name=company_name)
        flag = ""
        n=User_Det.count()
        profile =[]
        re_ = []
        st =[]
        
        print(User_Det)
        for u_ ,i in zip(User_Det,range(n)):
            profile.append(job_seeker.objects.all().values('f_name','l_name','gender','state','u_name','city','js_profile_pic','email_id').get(u_name=u_['va_u_name']))
            x=viewApplicants_1.objects.all().values('va_resume','va_status').filter(va_job_id=job_id,va_company_name=company_name,va_u_name=u_['va_u_name'])
            re_.append(x[0]['va_resume'])
            st.append(x[0]['va_status'])
        #print(re_[1][0]['va_resume'],profile[0])
    return render(request,'view_applications.html',{'path':path,'u_name':u_name,'flag':flag,'company_id':company_id,'profile':zip(profile,re_,st),'company_name':company_name,'job_id':job_id})

def CJD(request):
    if request.method == 'POST':
        path = request.POST['path']
        category = request.POST['category']
        position = request.POST['position']
        requirment = request.POST['requirment']
        company_name = request.POST['company_name']
        location = request.POST['location']
        start_date =request.POST['start_date']
        duration =request.POST['duration']
        salary =request.POST['salary']
        posted_on =request.POST['posted_on']
        apply_by = request.POST['apply_by']
        description =request.POST['description']
        perks =request.POST['perks']
        vacancy =request.POST['vacancy']
        experience =request.POST['experience']
        u_name = request.POST['u_name']
        user_det = request.POST['user_det']
        job_id = request.POST['job_id']
        print(apply_by , description)
        return render(request,'comp_job_det.html',{'requirment':requirment,'path':path,'category':category,'position':position,'company_name':company_name,'location':location,'start_date':start_date,'duration':duration,'salary':salary,'posted_on':posted_on,'apply_by':apply_by,'description':description,'perks':perks,'vacancy':vacancy,'experience':experience,'u_name':u_name,'user_det':user_det,'job_id':job_id})

def HJD(request):
    if request.method == 'POST':
        path = request.POST['path']
        company_name = request.POST['company_name']
        job_id = request.POST['job_id']
        company_id = request.POST['company_id']
        u_name = request.POST['u_name']
        JD = job_details.objects.all().values('jd_position','jd_location','jd_skills_required','jd_category','jd_salary','jd_vacancy','jd_experience','jd_perks','jd_description','jd_start_date','jd_apply_by','jd_posted_on','jd_duration').get(jd_job_id=job_id,jd_company_id=company_id,jd_company_name=company_name)    
        jd_start_date = str(JD['jd_start_date'])
        jd_apply_by = str(JD['jd_apply_by'])
        jd_position = JD['jd_position']
        jd_category = JD['jd_category']
        return render(request,'update_JD.html',{'path':path,'jd_position':jd_position,'jd_category':jd_category,'jd_start_date':jd_start_date,'jd_apply_by':jd_apply_by,'JD':JD,'company_name':company_name,'job_id':job_id,'company_id':company_id,'u_name':u_name})

def UPJD(request):
    if request.method == 'POST':
        reset = request.POST['reset']
        if reset == "reset":
            path = request.POST['path']
            company_name = request.POST['company_name']
            job_id = request.POST['job_id']
            company_id = request.POST['company_id']
            u_name = request.POST['u_name']
            jd_posted_on = request.POST['jd_posted_on']
            JD = job_details.objects.all().values('jd_position','jd_location','jd_skills_required','jd_category','jd_salary','jd_vacancy','jd_experience','jd_perks','jd_description','jd_start_date','jd_apply_by','jd_posted_on','jd_duration').get(jd_job_id=job_id,jd_company_id=company_id,jd_company_name=company_name)    
            jd_start_date = str(JD['jd_start_date'])
            jd_apply_by = str(JD['jd_apply_by'])
            jd_position = JD['jd_position']
            jd_category = JD['jd_category']
            return render(request,'update_JD.html',{'path':path,'jd_position':jd_position,'jd_category':jd_category,'jd_start_date':jd_start_date,'jd_apply_by':jd_apply_by,'JD':JD,'company_name':company_name,'job_id':job_id,'company_id':company_id,'u_name':u_name})
        elif reset == "delete":
            path = request.POST['path']
            company_name = request.POST['company_name']
            job_id = request.POST['job_id']
            company_id = request.POST['company_id']
            u_name = request.POST['u_name']
            jd_posted_on = request.POST['jd_posted_on']

            job_details.objects.get(jd_job_id=job_id,jd_company_id=company_id,jd_company_name=company_name).delete()
            viewApplicants.objects.filter(va_company_name=company_name,jd_job_id=job_id).delete()
            viewApplicants_1.objects.filter(va_company_name=company_name,jd_job_id=job_id).delete()
            #print(x,type(x))
            #viewApplicants_1.objects.get(id=ID1['id'],va_job_id =job_id,va_company_name=company_name,va_u_name= u_name,va_resume=resume,va_status=status).delete()
            company_id = job_provider.objects.all().values('job_provider_company_id').get(job_provider_company_id = company_id)
            profile = company.objects.all().values('company_logo','company_name','company_id').get(company_id=company_id['job_provider_company_id'])
            if job_details.objects.exists():
                Job_Det = job_details.objects.all().values('jd_job_id','jd_category','jd_company_name','jd_location','jd_position','jd_salary','jd_start_date','jd_apply_by','jd_posted_on','jd_duration').filter(jd_company_id=company_id['job_provider_company_id'],jd_company_name=profile['company_name'])
                    
            else:
                Job_Det = "No Applications Yet!!"
                    
            return render(request,'jp_hpage.html',{'company_name':profile['company_name'],'path':profile['company_logo'],'company_id':profile['company_id'],'Job_Det':Job_Det,'u_name':u_name})
        else:
            jd_company_id = request.POST['company_id']
            jd_company_name = request.POST['company_name']
            jd_job_id = request.POST['jd_job_id']
            jd_position = request.POST['jd_position']
            jd_location = request.POST['jd_location']
            jd_skills_required = request.POST['jd_skills_required']
            jd_category = request.POST['jd_category']
            jd_salary = request.POST['jd_salary']
            jd_vacancy =request.POST['jd_vacancy']
            jd_experience =request.POST['jd_experience']
            jd_description =request.POST['jd_description']
            jd_start_date = request.POST['jd_start_date']
            jd_apply_by = request.POST['jd_apply_by']
            jd_posted_on = request.POST['jd_posted_on']
            jd_duration = request.POST['jd_duration']
            jd_perks = request.POST['jd_perks']
            u_name = request.POST['u_name']
            
            storeInTable1 = job_details(jd_company_id=jd_company_id,jd_company_name=jd_company_name,jd_job_id=jd_job_id,jd_position=jd_position,jd_location=jd_location,jd_skills_required=jd_skills_required,jd_category=jd_category,jd_salary=jd_salary,jd_vacancy=jd_vacancy,jd_experience=jd_experience,jd_description=jd_description,jd_start_date=jd_start_date,jd_apply_by=jd_apply_by,jd_posted_on=jd_posted_on,jd_duration=jd_duration,jd_perks=jd_perks)
            storeInTable1.save()
            company_id = job_provider.objects.all().values('job_provider_company_id').get(job_provider_company_id = jd_company_id)
            profile = company.objects.all().values('company_logo','company_name','company_id').get(company_id=company_id['job_provider_company_id'])
            
            if job_details.objects.exists():
                Job_Det = job_details.objects.all().values('jd_job_id','jd_category','jd_company_name','jd_location','jd_position','jd_salary','jd_start_date','jd_apply_by','jd_posted_on','jd_duration').filter(jd_company_id=company_id['job_provider_company_id'],jd_company_name=profile['company_name'])
                    
            else:
                Job_Det = "No Applications Yet!!"
                    
            return render(request,'jp_hpage.html',{'company_name':profile['company_name'],'path':profile['company_logo'],'company_id':profile['company_id'],'Job_Det':Job_Det,'u_name':u_name})
      
    else:

        return render(request,'Job_Details.html')


def Jstatus(request):
    if request.method == 'POST':
        u_name = request.POST['u_name']
        user_det = request.POST['user_det']
        App_job = viewApplicants.objects.all().values('va_job_id','va_company_name','va_resume','va_status').filter(va_u_name=u_name)
        Job_Det = []
        com_logo =[]
        st = []
        jobD = []
        c = []
        print(u_name)
        print(App_job)
        if job_details.objects.exists():
            for a_ in App_job:
                com_logo.append(company.objects.all().values('company_logo').get(company_name=a_['va_company_name']))
                Job_Det.append(job_details.objects.all().values('jd_position','jd_location','jd_category').get(jd_job_id=a_['va_job_id'],jd_company_name=a_['va_company_name']))
                st.append(a_['va_status'])
                jobD.append(a_['va_job_id'])
                c.append(a_['va_company_name'])
        

        return render(request,'js_status.html',{'user_det':user_det,'u_name':u_name,'Detail':zip(com_logo,Job_Det,st,jobD,c)})

def UpResume(request):
    if request.method == 'POST':
        resume = request.FILES.get('resume','xyz.pdf')
        print(resume)
        u_name = request.POST['u_name']
        position = request.POST['position']
        company_name = request.POST['company_name']
        category = request.POST['category']
        user_det = request.POST['user_det']
        job_id = request.POST['job_id']
        path = 'static/Resume/'
        file_ = u_name + "_" + company_name + category
        format_ = os.path.join(path, file_)
        file_extension = os.path.splitext(resume.name)[1]
        file_save_path = format_ + file_extension
        print(job_id)
        storeInTable1 = viewApplicants(va_job_id =job_id,va_company_name=company_name,va_u_name= u_name,va_resume=file_save_path)
        storeInTable1.save()
        storeInTable2 = viewApplicants_1(va_job_id =job_id,va_company_name=company_name,va_u_name= u_name,va_resume=file_save_path)
        storeInTable2.save()

        with open(file_save_path, 'wb+') as f:
            for chunk in resume.chunks():
                f.write(chunk)

            
    return HJS(request,u_name,user_det)

def Accept(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        company_id = request.POST['company_id']
        job_id = request.POST['job_id']
        u_name = request.POST['u_name']
        u_nameJP = request.POST['u_nameJP']
        resume = request.POST['resume']
        status = request.POST['status']
        path = request.POST['path']
        flag = request.POST['flag']
        ID = viewApplicants.objects.all().values('id').get(va_job_id =job_id,va_company_name=company_name,va_u_name= u_name,va_resume=resume)
        ID1 = viewApplicants_1.objects.all().values('id').get(va_job_id =job_id,va_company_name=company_name,va_u_name= u_name,va_resume=resume)
        
        storeInTable1 = viewApplicants(id=ID['id'],va_job_id =job_id,va_company_name=company_name,va_u_name= u_name,va_resume=resume,va_status=status)
        storeInTable1.save()
        storeInTable2 = viewApplicants_1(id=ID1['id'],va_job_id =job_id,va_company_name=company_name,va_u_name= u_name,va_resume=resume,va_status=status)
        storeInTable2.save()
        viewApplicants_1.objects.get(id=ID1['id'],va_job_id =job_id,va_company_name=company_name,va_u_name= u_name,va_resume=resume,va_status=status).delete()
        User_Det = viewApplicants_1.objects.all().values('va_u_name','va_resume','va_status').filter(va_job_id=job_id,va_company_name=company_name)
        
        n=User_Det.count()
        profile =[]
        re_ = []
        st =[]
        for u_ ,i in zip(User_Det,range(n)):
            profile.append(job_seeker.objects.all().values('f_name','l_name','gender','state','u_name','city','js_profile_pic','email_id').get(u_name=u_['va_u_name']))
            x=viewApplicants_1.objects.all().values('va_resume','va_status').filter(va_job_id=job_id,va_company_name=company_name,va_u_name=u_['va_u_name'])
            re_.append(x[i]['va_resume'])
            st.append(x[i]['va_status'])
    return render(request,'view_applications.html',{'path':path,'flag':flag,'u_name':u_nameJP,'profile':zip(profile,re_,st),'company_name':company_name,'company_id':company_id,'job_id':job_id})
    
def EditPP(request):
    if request.method == 'POST':
        pro = request.POST['pro']
        company_id = request.POST['company_id']
        path = request.POST['path']
        u_name = request.POST['u_name']

        if pro == "remove":
            img_save_path = 'static/Company_Logo/symbol.png'
        else:
            company_logo = request.FILES.get('company_logo','symbol.png')
            
            
            if company_logo != 'symbol.png':
                path = 'static/Company_Logo/'
                format_ = os.path.join(path, company_id)
                img_extension = os.path.splitext(company_logo.name)[1]
                img_save_path = format_ + img_extension
                with open(img_save_path, 'wb+') as f:
                    for chunk in company_logo.chunks():
                        f.write(chunk)
            else:
                
                img_save_path = 'static/Company_Logo/symbol.png'


        CP = company.objects.all().values('company_id','company_name','company_type','company_state','company_city','company_add','company_pincode','company_mobile_no','company_email_id','company_url').get(company_id=company_id)
        storeInTable1 = company(company_id=company_id,company_name=CP['company_name'],company_type=CP['company_type'],company_state=CP['company_state'],company_city=CP['company_city'],company_add=CP['company_add'],company_pincode=CP['company_pincode'],company_mobile_no=CP['company_mobile_no'],company_email_id=CP['company_email_id'],company_url=CP['company_url'],company_logo=img_save_path)
        storeInTable1.save()
        flag=""
        profile = company.objects.all().values('company_logo','company_name').get(company_id=company_id)
                
        if job_details.objects.exists():
            Job_Det = job_details.objects.all().values('jd_job_id','jd_category','jd_company_name','jd_location','jd_position','jd_salary','jd_start_date','jd_apply_by','jd_posted_on','jd_duration').filter(jd_company_id=company_id,jd_company_name=profile['company_name'])
        path =  img_save_path
        return render(request,'jp_hpage.html',{'company_name':profile['company_name'],'flag':flag,'u_name':u_name,'path':path,'company_id':company_id,'Job_Det':Job_Det})

def EditJS(request):
    if request.method == 'POST':
        
        user_det = request.POST['user_det']
        u_name = request.POST['u_name'] 
        pro = request.POST['pro']
        if pro == "remove":
            img_save_path = 'static/User_profile/profile.png'
        else:
            js_profile_pic = request.FILES.get('js_profile_pic','profile.png')
            print(js_profile_pic)
            if js_profile_pic != 'profile.png':
                path = 'static/User_profile/'
                format_ = os.path.join(path, u_name)
                img_extension = os.path.splitext(js_profile_pic.name)[1]
                img_save_path = format_ + img_extension
                with open(img_save_path, 'wb+') as f:
                    for chunk in js_profile_pic.chunks():
                        f.write(chunk)
            else:
                
                img_save_path = 'static/User_profile/profile.png'

        JS = job_seeker.objects.all().values('f_name','m_name','l_name','gender','uid_type','uid_number','dob','state','city','add','pincode','email_id','mobile_no','pwd','u_name','js_security_question','js_ans_security_question','js_profile_pic').get(u_name=u_name)
        storeInTable = job_seeker(f_name=JS['f_name'],l_name=JS['l_name'],m_name=JS['m_name'],gender=JS['gender'],uid_type=JS['uid_type'],uid_number=JS['uid_number'],dob=JS['dob'],state=JS['state'],email_id=JS['email_id'],mobile_no=JS['mobile_no'],pwd=JS['pwd'],u_name=JS['u_name'],pincode=JS['pincode'],city=JS['city'],add=JS['add'],js_security_question=JS['js_security_question'],js_ans_security_question=JS['js_ans_security_question'],js_profile_pic=img_save_path)
        storeInTable.save()
        flag=""
        user_det = img_save_path
        return HJS(request,u_name,user_det)
                
        
        
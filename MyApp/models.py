from django.db import models
from django.utils.timezone import now
# Create your models here.
class users(models.Model):
    user_type = models.CharField(max_length=50)
    u_name = models.CharField(max_length=50 , primary_key=True)
    pwd = models.CharField(max_length=12)


class job_seeker(models.Model):
    f_name = models.CharField(max_length=50)
    m_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    uid_type = models.CharField(max_length=50)
    uid_number = models.CharField(max_length=20,primary_key=True)
    dob = models.DateField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    add = models.CharField(max_length=70)
    pincode = models.CharField(max_length=10)
    email_id = models.EmailField()
    mobile_no = models.CharField(max_length=11)
    pwd = models.CharField(max_length=12)
    u_name = models.CharField(max_length=50 , unique=True)
    js_security_question = models.CharField(max_length=100,default='DEFAULT VALUE')
    js_ans_security_question = models.CharField(max_length=50,default='DEFAULT VALUE')
    js_profile_pic = models.ImageField(upload_to='static/User_profile' ,default='static/User_profile/profile.png')

class company(models.Model):
    company_id = models.CharField(max_length=11,primary_key=True)
    company_name = models.CharField(max_length=50)
    company_type = models.CharField(max_length=50)
    company_state = models.CharField(max_length=50)
    company_city = models.CharField(max_length=20)
    company_add = models.CharField(max_length=70)
    company_pincode = models.CharField(max_length=10)
    company_mobile_no = models.CharField(max_length=11)
    company_email_id = models.EmailField()
    company_url = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='static/Company_Logo' ,default='static/Company_Logo/symbol.png')
    
class job_provider(models.Model):
    job_provider_company_id = models.CharField(max_length=11, primary_key=True)
    job_provider_fname = models.CharField(max_length=50)
    job_provider_mname = models.CharField(max_length=50)
    job_provider_lname = models.CharField(max_length=50)
    job_provider_gender = models.CharField(max_length=20)
    job_provider_position = models.CharField(max_length=20 ,default='DEFAULT VALUE')
    u_name = models.CharField(max_length=50,default='DEFAULT VALUE')
    pwd = models.CharField(max_length=12,default='DEFAULT VALUE')
    jp_security_question = models.CharField(max_length=100,default='DEFAULT VALUE')
    jp_ans_security_question = models.CharField(max_length=50,default='DEFAULT VALUE')
     
class job_details(models.Model):
    jd_company_id = models.CharField(max_length=11)
    jd_company_name = models.CharField(max_length=50)
    jd_job_id = models.CharField(max_length=11,primary_key=True)
    jd_position = models.CharField(max_length=20)
    jd_location = models.CharField(max_length=50)
    jd_skills_required = models.CharField(max_length=50)
    jd_category = models.CharField(max_length=50)
    jd_salary = models.CharField(max_length=10)
    jd_vacancy = models.IntegerField()
    jd_experience = models.IntegerField()
    jd_perks = models.CharField(max_length=50,default='DEFAULT VALUE')
    jd_description = models.CharField(max_length=300)
    jd_start_date = models.DateField(blank=True,null=True,default=now)
    jd_apply_by = models.DateField(blank=True,null=True,default=now)
    jd_posted_on = models.CharField(max_length=15,null=True)
    jd_duration = models.CharField(max_length=20,null=True) 

class viewApplicants(models.Model):
    va_job_id = models.CharField(max_length=11,default = 'Default')
    va_u_name = models.CharField(max_length=50)
    va_company_name = models.CharField(max_length=50)
    va_resume = models.FileField(upload_to='static/Resume',null=True)
    va_status = models.CharField(max_length=20,default="Pending")

class viewApplicants_1(models.Model):
    va_job_id = models.CharField(max_length=11,default = 'Default')
    va_u_name = models.CharField(max_length=50)
    va_company_name = models.CharField(max_length=50)
    va_resume = models.FileField(upload_to='static/Resume',null=True)
    va_status = models.CharField(max_length=20,default="Pending")
    #class Meta:
    #    unique_together = ("field1", "field2")

class contact_us(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    query = models.CharField(max_length=200)
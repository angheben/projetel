from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def send_mail(self):
        name = self.cleaned_data['Name']
        email = self.cleaned_data['Email']
        subject = self.cleaned_data['Subject']
        message = self.cleaned_data['Message']

        content = f'Name: {name} \n' \
                  f'E-mail: {email} \n' \
                  f'Subject: {subject} \n' \
                  f'Message: {message} '
        mail = EmailMessage(
            subject=subject,
            body=content,
            from_email='contact@fusion.com.br',
            to=['contact@fusion.com.br'],
            headers={'Reply-To': email}
        )
        mail.send()
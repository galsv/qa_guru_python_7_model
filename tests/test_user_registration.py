from model import controls
from model.pages import registration_form
from tests.test_data.users import user, Subject, Hobby



def test_submit_student_registration_form():
    registration_form.given_opened()

    registration_form.set_first_name(user.name)
    registration_form.set_last_name(user.last_name)
    registration_form.set_email(user.email)
    registration_form.set_gender(user.gender)
    registration_form.set_user_number(user.user_number)
    registration_form.set_date_of_birthday(user.date)
    registration_form.add_subjects(user.subjects)
    registration_form.select_hobbies_cb(user.hobbies)
    registration_form.upload_picture(user.picture_file)
    registration_form.set_current_address(user.current_address)
    registration_form.scroll_to_bottom()
    registration_form.set_state(user.state)
    registration_form.set_city(user.city)

    controls.submit.click_sbmt()

    registration_form.should_have_submitted(
        [
            ('Student Name', f'{user.name} {user.last_name}'),
            ('Student Email', user.email),
            ('Gender', user.gender),
            ('Mobile', user.user_number),
            ('Date of Birth', '10 October,1984'),
            ('Subjects', Subject.History.value),
            ('Hobbies', Hobby.Sports.name),
            ('Picture', user.picture_file),
            ('Address', user.current_address),
            ('State and City', f'{user.state} {user.city}')
        ],
    )


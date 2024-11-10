from django import forms

class ReleaseForm(forms.Form):
    ArtistName = forms.CharField(widget=forms.TextInput({'placeholder':'Artist Name', 'autocomplete':'off'}))
    FeaturedArtist = forms.CharField(widget=forms.TextInput({'placeholder':'R kelly, Michael Jack', 'autocomplete':'off'}))
    SongWriters = forms.CharField(widget=forms.TextInput({'placeholder':'Label Name', 'autocomplete':'off'}))
    Producers = forms.CharField(widget=forms.TextInput({'placeholder':'Producers', 'autocomplete':'off'}))
    MusicType = forms.CharField(widget=forms.TextInput({'placeholder':'Song-Name/Ep-Name/Album-Name/', 'autocomplete':'off'}))
    ReleaseDate = forms.DateField(widget=forms.DateInput({'type':'date', 'placeholder':'Release Date', 'autocomplete':'off'}))
    RadioChoices = [
        ('single', 'Single'),
        ('album', 'Album'),
        ('ep', 'EP')
    ]
    Type = forms.ChoiceField(choices=RadioChoices, widget=forms.RadioSelect, label="Type")

    # RadioChoices = [
    #     ('Male', 'Male'),
    #     ('Female', 'Female'),
        
    # ]
    # Type = forms.ChoiceField(choices=RadioChoices, widget=forms.RadioSelect, label="Type")

    FileUpload = forms.FileField(widget=forms.ClearableFileInput(attrs={'placeholder': 'Choose a file'}),label="Upload Music")
    # MultipleFileUpload = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),label="Upload Files")
    CoverArt = forms.FileField(widget=forms.ClearableFileInput(attrs={'placeholder': 'Choose a file'}),label="Upload Cover Art")
    Muamala = forms.FileField(widget=forms.ClearableFileInput(attrs={'placeholder': 'Screen-shot'}),label="Upload Screen-shot ya Muamala")
    PhoneNumber = forms.CharField(
    widget=forms.TextInput(attrs={'type': 'tel','placeholder': 'Phone Number','autocomplete': 'off','pattern': '[0-9]{3}-[0-9]{3}-[0-9]{4}','title': 'Enter a phone number in the format: XXX-XXX-XXXX'}),label="Phone Number")
    Email = forms.EmailField(widget=forms.EmailInput({'placeholder':'email', 'autocomplte':'off'}))

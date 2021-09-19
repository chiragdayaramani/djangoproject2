

document.getElementById('id_cover_pic').onchange=(e)=>{
    imageField = e.target;
    console.log(imageField);
    if(imageField.files && imageField.files[0]){
        
        let fileReader=new FileReader()

        fileReader.readAsDataURL(imageField.files[0]);
        fileReader.onload=(e)=>{
            
            let imagePreview=document.getElementById('img-preview');
            console.log(imagePreview);
            imagePreview.setAttribute('src',e.target.result);
        }
    }
}
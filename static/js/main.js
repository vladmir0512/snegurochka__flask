var sex_select = document.getElementById("sex");
var name_select = document.getElementById("name");
var file1_upload = document.getElementById("file1");
var file2_upload = document.getElementById("file2");
var file3_upload = document.getElementById("file3");

var file1_block = document.getElementById("file1_block");
var file2_block = document.getElementById("file2_block");
var file3_block = document.getElementById("file3_block");


sex_select.onchange = function()  {

    sex = sex_select.value;

    fetch('/name/' + sex).then(function(response) {

        response.json().then(function(data) {
           let optionHTML = '';

           for (let name of data.names){
                optionHTML += '<option value="' + name.id + '">' + name.name + '</option>';

           }

        name_select.innerHTML = optionHTML;	

        })
        
    });
};


file1_upload.onchange = evt => {
  
  
const formData = new FormData();

formData.append('photo', file1_upload.files[0]);

const options = {
  method: 'POST',
  body: formData,
  // If you add this, upload won't work
//   headers: {
//     'Content-Type': 'multipart/form-data',
//   }
};
    const url = '/prev';
    fetch(url,options)
    .then(response => response.json())  
    .then(json => {
        console.log(json["json"]);
        optionHTML = '';
        optionHTML += '<img src="data:image/png;base64, ' + json["json"] +'"    width=370 height=180  alt="фото2"><p class="font-weight-normal">Предпросмотр первого фото</p><br>';
       
        file1_block.innerHTML = optionHTML;
    });
             
        };
        



file2_upload.onchange = evt => {
     
const formData = new FormData();

formData.append('photo', file2_upload.files[0]);

const options = {
  method: 'POST',
  body: formData,
  // If you add this, upload won't work
//   headers: {
//     'Content-Type': 'multipart/form-data',
//   }
};
    const url = '/prev';
    fetch(url,options)
    .then(response => response.json())  
    .then(json => {
        console.log(json["json"]);
        optionHTML = '';
        optionHTML += '<img src="data:image/png;base64, ' + json["json"] +'"    width=370 height=180  alt="фото2"><p class="font-weight-normal" >Предпросмотр второго фото</p><br>';
       
        file2_block.innerHTML = optionHTML;
    });
             
};


file3_upload.onchange = evt => {
    const formData2 = new FormData();

    formData2.append('photo1', file3_upload.files[0]);
    
    const options = {
      method: 'POST',
      body: formData2
      // If you add this, upload won't work
    //   headers: {
    //     'Content-Type': 'multipart/form-data',
    //   }
    };
        const url = '/prevv';
        fetch(url,options)
        .then(response => response.json())  
        .then(json => {
            console.log(json["json"]);
            optionHTML = '';
            optionHTML += '<img src="data:image/png;base64, ' + json["json"] +'"   width=370 height=180  alt="фото_письма"><p class="font-weight-normal">Предпросмотр фото письма</p><br>';
           
            file3_block.innerHTML = optionHTML;
        });
                 
};

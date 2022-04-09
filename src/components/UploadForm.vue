<template>
  <form @submit.prevent="uploadPhoto" id="uploadForm">
    <input type="text" name="photo"/>
    <input type="file" name="description"/>
    <input type="submit" />
  </form>
</template>
<script>
export default {
  created() {
    console.log("Created");
  },
  methods: {
    uploadPhoto() {

    
      let uploadForm = document.getElementById("uploadForm");

      console.log(uploadForm)
      let form_data = new FormData(uploadForm);

      console.log(form_data)

      fetch("/api/upload", {
        method: "POST",
        body:form_data
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          // display a success message
          console.log(data);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>

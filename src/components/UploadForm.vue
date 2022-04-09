<template>
  <form @submit.prevent="uploadPhoto" id="uploadForm">
    <input type="text" name="photo" />
    <input type="file" name="description" />
    <input type="submit" />
  </form>
</template>
<script>
export default {
  created() {
    this.getCsrfToken();
  },
  data: () => {
    return {
      csrf_token: "",
    };
  },
  methods: {
    getCsrfToken() {
      let self = this;
      fetch("/api/csrf-token")
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          self.csrf_token = data.csrf_token;
        });
    },
    uploadPhoto() {
      let uploadForm = document.getElementById("uploadForm");

      console.log(uploadForm);
      let form_data = new FormData(uploadForm);

      console.log(form_data);

      fetch("/api/upload", {
        method: "POST",
        body: form_data,
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
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

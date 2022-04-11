<template>
  <div class="container">
    <form @submit.prevent="uploadPhoto" id="uploadForm" class="row">
      <div class="col col-lg-6 col-md-6 col-sm-12">
        <h1>Upload Photo</h1>
      </div>
      <div
        v-if="uploadSuccess"
        class="col col-lg-6 col-md-6 col-sm-12 alert alert-success"
      >
        File Upload Successful
      </div>
      <div
        v-if="uploadError"
        class="col col-lg-6 col-md-6 col-sm-12 alert alert-danger"
      >
        <ul>
          <li v-for="error in formErrors" :key="error">{{ error }}</li>
        </ul>
      </div>
      <div class="form-group col col-lg-6 col-md-6 col-sm-12">
        <label for="exampleInputPassword1">Photo</label>
        <input type="file" name="photo" class="form-control" id="photo" />
      </div>

      <div
        class="form-group col col-lg-6 col-md-6 col-sm-12"
        style="margin-bottom: 20px"
      >
        <label for="Description">Description</label>
        <textarea
          type="text"
          name="description"
          class="form-control"
          id="Description"
          placeholder="Description"
        ></textarea>
      </div>
      <br />
      <div class="form-group col col-lg-6 col-md-6 col-sm-12">
        <button type="submit" class="btn btn-primary">Upload Photo</button>
      </div>
    </form>
  </div>
</template>
<script>
export default {
  created() {
    this.getCsrfToken();
  },
  data: () => {
    return {
      csrf_token: "",
      uploadSuccess: false,
      formErrors: [],
      uploadError: false,
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
      const self = this;

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
          if ("errors" in data) {
            self.uploadError = true;
            self.uploadSuccess = false;
            self.formErrors = [...data.errors];
          } else {
            self.uploadError = false;
            self.uploadSuccess = true;
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
#uploadForm {
  display: flex;
  min-height: 400px;
  flex-direction: column;
  padding: 30px;
  align-items: center;
}
</style>
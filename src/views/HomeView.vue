<script>
import UploadForm from "./../components/UploadForm.vue";
export default {
  data() {
    return {
      message: "Hello World! This is Lab 7",
    };
  },

  components: {UploadForm},
};
</script>

<template>
  <div class="container">
    <div class="text-center">
      <UploadForm></UploadForm>

      <img
        alt="Vue logo"
        class="logo"
        src="@/assets/logo.svg"
        width="125"
        height="125"
      />
      <h1>{{ message }}</h1>
    </div>
  </div>
</template>

<style>
/* Add any component specific styles here */
</style>
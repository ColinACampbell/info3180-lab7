<template>
  <UploadForm />
</template>
<script>
import UploadForm from "./../components/UploadForm.vue";

export default {
  components: { UploadForm },
  created() {
      this.getCsrfToken()
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
  },
};
</script>

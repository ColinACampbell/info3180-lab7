<template>
  <form @submit.prevent="uploadPhoto">
      <input type="text"/>
      <input type="file"/>
      <input type="submit"/>
  </form>
</template>
<script>
export default {
  created() {
    console.log("Created");
  },
  methods: {
    uploadPhoto() {
      fetch("/api/upload", {
        method: "POST",
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

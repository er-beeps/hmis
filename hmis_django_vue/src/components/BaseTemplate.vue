<template>
  <!DOCTYPE html>
  <html>
    <head>
      <title>HMIS</title>
      <link
        rel="shortcut icon"
        type="image/jpg"
        href="../assets/images/hospital.png"
      />

      <meta charset="utf-8" />
      <meta http-equiv="X-UA-COMPATIBLE" content="IE=edge" />
      <meta
        content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"
        name="viewport"
      />
    </head>

    <body class="hold-transition sidebar-mini layout-fixed text-sm">
      <navigation-headbar></navigation-headbar>
      <navigation-sidebar></navigation-sidebar>

    </body>
  </html>
</template>


<script>
import NavigationHeadbar from "./NavigationHeadbar.vue";
import NavigationSidebar from "./NavigationSidebar.vue";

export default {
  name: "BaseTemplate",
  components: {
    NavigationHeadbar,
    NavigationSidebar
  },
};
</script>
<style>
@import "https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css";
@import "https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700";

@import "../../../adminlte3/static/admin-lte/plugins/fontawesome-free/css/all.min.css";
@import "../../../adminlte3/static/admin-lte/dist/css/adminlte.min.css";
@import "../../../adminlte3/static/admin-lte/plugins/icheck-bootstrap/icheck-bootstrap.min.css";

@import "../assets/styles/noty.css";
@import "../assets/styles/custom.css";
@import "../assets/styles/nepali.datepicker.v3.5.min.css";
</style>
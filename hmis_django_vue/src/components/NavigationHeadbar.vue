<template>
  <div class="navigation-headbar">
    <nav class="main-header navbar navbar-expand navbar-dark navbar-secondary">
      <!-- Header Navbar: style can be found in header.less -->
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link toggle-navbar" data-widget="pushmenu" href="#"
            ><i class="fas fa-bars"></i
          ></a>
        </li>
        <li class="nav-item d-none d-sm-inline-block">
          <navigation-link url="/homepage">Data Master</navigation-link>
          <!-- <a href="{% url 'homepage' %}" class="nav-link">Data Master</a> -->
        </li>
      </ul>

      <!-- Right navbar links -->
      <ul class="navbar-nav ml-auto">
        <li class="nav-item dropdown user-menu">
          <a
            href="#"
            class="nav-link dropdown-toggle"
            data-toggle="dropdown"
            aria-expanded="true"
          >
            <img
              src="#"
              class="user-image img-circle elevation-2"
              alt="User Image"
            />
            <!-- <span class="d-none d-md-inline">{% firstof request.user.get_username %}</span -->
            >
          </a>
          <ul class="dropdown-menu dropdown-menu-lg dropdown-menu-right">
            <!-- User image -->
            <li class="user-header bg-primary">
              <img src="#" class="img-circle elevation-2" alt="User Image" />

              <!-- <p>
                        {% firstof request.user.get_short_name request.user.get_username %} - {% firstof request.user.get_role %}
                      <small>Member since : {{ request.user.date_joined }}</small>
                    </p> -->
            </li>
            <!-- Menu Body -->
            <li class="user-body">
              <div class="row">
                <div class="col-4 text-center">
                  <a href="#">Profile</a>
                </div>
                <div class="col-4 text-center">
                  <a href="#">Team</a>
                </div>
                <div class="col-4 text-center">
                  <a href="#">Friends</a>
                </div>
              </div>
              <!-- /.row -->
            </li>
            <!-- Menu Footer-->
            <li class="user-footer">
              <!-- <a href="{% url 'logout' %}" class="btn btn-default btn-flat float-right">{% trans 'Sign Out'%}<a> -->
            </li>
          </ul>
        </li>
      </ul>
    </nav>
  </div>
</template>
<script>
import NavigationLink from "./partial-components/navigation-link.vue";
export default {
  name: "NavigationHeadbar",
  components: {
    NavigationLink,
  },
};
</script>
<style>
</style>
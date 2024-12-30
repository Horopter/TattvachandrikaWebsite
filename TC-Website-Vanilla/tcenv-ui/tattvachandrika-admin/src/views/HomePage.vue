<template>
  <div class="container mt-5">
    <h1>Welcome to Tattvachandrika Admin Portal</h1>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item active" aria-current="page">Home</li>
      </ol>
    </nav>
    <ul class="list-group">
      <li class="list-group-item"><router-link to="/subscription-modes">Manage Subscription Modes</router-link></li>
      <li class="list-group-item"><router-link to="/subscription-languages">Manage Subscription Languages</router-link></li>
      <li class="list-group-item"><router-link to="/subscriber-categories">Manage Subscriber Categories</router-link></li>
      <li class="list-group-item"><router-link to="/subscriber-types">Manage Subscriber Types</router-link></li>
      <li class="list-group-item"><router-link to="/subscription-plans">Manage Subscription Plans</router-link></li>
      <li class="list-group-item"><router-link to="/payment-modes">Manage Payment Modes</router-link></li>
      <li class="list-group-item"><router-link to="/subscribers">Manage Subscribers</router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
};
</script>

<style scoped>
/* Add your styles here */
</style>

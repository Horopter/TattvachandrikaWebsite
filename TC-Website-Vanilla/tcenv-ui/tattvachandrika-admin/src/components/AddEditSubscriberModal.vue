<template>
  <div v-if="show" class="modal fade show" tabindex="-1" role="dialog" style="display: block;">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">{{ modalTitle }}</h5>
          <button type="button" class="close" @click="close" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="handleSubmit">
            <div class="form-group">
              <label for="name">Name</label>
              <input type="text" class="form-control" id="name" v-model="localSubscriber.name" required>
            </div>
            <div class="form-group">
              <label for="registration_number">Registration Number</label>
              <input type="text" class="form-control" id="registration_number" v-model="localSubscriber.registration_number" required>
            </div>
            <div class="form-group">
              <label for="address">Address</label>
              <input type="text" class="form-control" id="address" v-model="localSubscriber.address">
            </div>
            <div class="form-group">
              <label for="city_town">City/Town</label>
              <input type="text" class="form-control" id="city_town" v-model="localSubscriber.city_town">
            </div>
            <div class="form-group">
              <label for="state">State</label>
              <input type="text" class="form-control" id="state" v-model="localSubscriber.state">
            </div>
            <div class="form-group">
              <label for="pincode">Pincode</label>
              <input type="text" class="form-control" id="pincode" v-model="localSubscriber.pincode">
            </div>
            <div class="form-group">
              <label for="phone">Phone</label>
              <input type="text" class="form-control" id="phone" v-model="localSubscriber.phone">
            </div>
            <div class="form-group">
              <label for="email">Email</label>
              <input type="email" class="form-control" id="email" v-model="localSubscriber.email" required>
            </div>
            <div class="form-group">
              <label for="category">Category</label>
              <select class="form-control" id="category" v-model="localSubscriber.category">
                <option v-for="category in categories" :value="category._id" :key="category._id">{{ category.name }}</option>
              </select>
            </div>
            <div class="form-group">
              <label for="stype">Type</label>
              <select class="form-control" id="stype" v-model="localSubscriber.stype">
                <option v-for="type in types" :value="type._id" :key="type._id">{{ type.name }}</option>
              </select>
            </div>
            <div class="form-group">
              <label for="notes">Notes</label>
              <textarea class="form-control" id="notes" v-model="localSubscriber.notes"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">{{ modalButton }}</button>
            <button type="button" class="btn btn-secondary" @click="close">Cancel</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: Boolean,
    subscriber: Object,
    categories: Array,
    types: Array
  },
  data() {
    return {
      localSubscriber: { ...this.subscriber }
    };
  },
  computed: {
    modalTitle() {
      return this.localSubscriber && this.localSubscriber._id ? 'Edit Subscriber' : 'Add Subscriber';
    },
    modalButton() {
      return this.localSubscriber && this.localSubscriber._id ? 'Update' : 'Add';
    }
  },
  watch: {
    subscriber(newVal) {
      this.localSubscriber = { ...newVal };
    }
  },
  methods: {
    close() {
      this.$emit('close');
    },
    handleSubmit() {
      this.$emit('save', this.localSubscriber);
      this.close();
    }
  }
};
</script>

<style scoped>
.modal {
  display: block;
  background-color: rgba(0, 0, 0, 0.5);
}
</style>

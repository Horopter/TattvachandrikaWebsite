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
              <label for="start_date">Start Date</label>
              <input type="date" class="form-control" id="start_date" v-model="localSubscription.start_date" required>
            </div>
            <div class="form-group">
              <label for="subscription_plan">Subscription Plan</label>
              <select class="form-control" id="subscription_plan" v-model="localSubscription.subscription_plan" required>
                <option v-for="plan in subscriptionPlans" :value="plan._id" :key="plan._id">{{ plan.name }}</option>
              </select>
            </div>
            <div class="form-group">
              <label for="payment_status">Payment Status</label>
              <select class="form-control" id="payment_status" v-model="localSubscription.payment_status" required @change="confirmPaymentStatus">
                <option value="Pending">Pending</option>
                <option value="Failed">Failed</option>
                <option value="Paid">Paid</option>
              </select>
            </div>
            <div class="form-group">
              <label for="payment_mode">Payment Mode</label>
              <select class="form-control" id="payment_mode" v-model="localSubscription.payment_mode" required>
                <option v-for="mode in paymentModes" :value="mode._id" :key="mode._id">{{ mode.name }}</option>
              </select>
            </div>
            <div class="form-group">
              <label for="payment_date">Payment Date</label>
              <input type="date" class="form-control" id="payment_date" v-model="localSubscription.payment_date" required>
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
import subscriptionPlanService from '../services/subscriptionPlanService';
import paymentModeService from '../services/paymentModeService';

export default {
  props: {
    show: Boolean,
    subscription: Object
  },
  data() {
    return {
      localSubscription: { ...this.subscription },
      subscriptionPlans: [],
      paymentModes: [],
      showConfirmationModal: false
    };
  },
  computed: {
    modalTitle() {
      return this.localSubscription && this.localSubscription._id ? 'Edit Subscription' : 'Add Subscription';
    },
    modalButton() {
      return this.localSubscription && this.localSubscription._id ? 'Update' : 'Add';
    }
  },
  watch: {
    subscription(newVal) {
      this.localSubscription = { ...newVal };
    }
  },
  created() {
    this.loadSubscriptionPlans();
    this.loadPaymentModes();
  },
  methods: {
    close() {
      this.$emit('close');
    },
    handleSubmit() {
      const payload = { ...this.localSubscription };
      delete payload.end_date;
      this.$emit('save', payload);
      this.close();
    },
    loadSubscriptionPlans() {
      subscriptionPlanService.getPlans().then(response => {
        this.subscriptionPlans = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription plans!", error);
      });
    },
    loadPaymentModes() {
      paymentModeService.getPaymentModes().then(response => {
        this.paymentModes = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the payment modes!", error);
      });
    },
    confirmPaymentStatus() {
      if (this.localSubscription.payment_status === 'Paid') {
        this.showConfirmationModal = true;
      }
    },
    handleConfirmation(confirm) {
      if (confirm) {
        this.localSubscription.payment_status = 'Paid';
      } else {
        this.localSubscription.payment_status = 'Pending';
      }
      this.showConfirmationModal = false;
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

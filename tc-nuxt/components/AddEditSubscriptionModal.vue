<template>
  <div v-if="show" class="fixed inset-0 z-50 flex items-center justify-center bg-gray-900 bg-opacity-50" tabindex="-1" role="dialog">
    <div class="bg-white rounded-lg shadow-lg w-full max-w-lg">
      <div class="flex justify-between items-center p-6 border-b">
        <h5 class="text-xl font-semibold text-gray-800">{{ modalTitle }}</h5>
        <button type="button" class="text-gray-600 hover:text-gray-900 transition" @click="close" aria-label="Close">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </div>
      <div class="p-6">
        <form @submit.prevent="handleSubmit">
          <div class="mb-4">
            <label for="start_date" class="block text-sm font-medium text-gray-700">Start Date</label>
            <input
              type="date"
              :min="currentDate"
              id="start_date"
              v-model="localSubscription.start_date"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2" 
              required
            >
          </div>

          <div class="mb-4">
            <label for="subscription_plan" class="block text-sm font-medium text-gray-700">Subscription Plan</label>
            <select
              id="subscription_plan"
              v-model="localSubscription.subscription_plan"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2" 
              required
            >
              <option v-for="plan in subscriptionPlans" :value="plan._id" :key="plan._id">{{ plan.name }}</option>
            </select>
          </div>

          <div class="mb-4">
            <label for="payment_status" class="block text-sm font-medium text-gray-700">Payment Status</label>
            <select
              id="payment_status"
              v-model="localSubscription.payment_status"
              @change="confirmPaymentStatus"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2"
              required
            >
              <option value="Pending">Pending</option>
              <option value="Failed">Failed</option>
              <option value="Paid">Paid</option>
            </select>
          </div>

          <div class="mb-4">
            <label for="payment_mode" class="block text-sm font-medium text-gray-700">Payment Mode</label>
            <select
              id="payment_mode"
              v-model="localSubscription.payment_mode"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2"
              required
            >
              <option v-for="mode in paymentModes" :value="mode._id" :key="mode._id">{{ mode.name }}</option>
            </select>
          </div>

          <div class="mb-4">
            <label for="payment_date" class="block text-sm font-medium text-gray-700">Payment Date</label>
            <input
              type="date"
              :min="currentDate"
              id="payment_date"
              v-model="localSubscription.payment_date"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2"
              required
            >
          </div>

          <div class="mb-4">
            <label for="payment_id" class="block text-sm font-medium text-gray-700">Payment ID (optional)</label>
            <input
              type="text"
              id="payment_id"
              v-model="localSubscription.payment_id"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2"
              placeholder="Enter payment ID"
            >
          </div>

          <div class="flex justify-end space-x-2">
            <button type="submit" class="px-5 py-2 bg-indigo-600 text-white font-semibold rounded-md shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition duration-150">{{ modalButton }}</button>
            <button type="button" class="px-5 py-2 bg-gray-300 text-gray-700 font-semibold rounded-md shadow-sm hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500 transition duration-150" @click="close">Cancel</button>
          </div>
        </form>
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
      currentDate: new Date().toISOString().split('T')[0],
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
/* Tailwind classes used; no additional CSS needed */
</style>

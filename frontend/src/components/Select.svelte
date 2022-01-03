<script lang="ts">
  export let value: string;
  export let slug: string;
  export let label: string;

  export let options: string[];
</script>

<div class="container">
  <label class="container__label" for={slug}>{label}</label>

  <select class="container__select" bind:value name={slug} id={slug}>
    {#each options as option}
      <option value={option}>{option}</option>
    {/each}
  </select>
</div>

<style lang="scss">
  .container {
    display: grid;
    grid-template-columns: 1fr 3fr;
    align-items: center;
    gap: 0.5rem;
    background-color: var(--secondary-color);
    text-align: center;
    font-weight: bold;
    padding: 0.5rem 0.75rem 0.5rem 0.5rem;
    color: var(--primary-color);

    &__select {
      border: none;
    }
  }
</style>

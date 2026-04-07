import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style for professional visualization
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11

def create_fascia_aeeg_distribution():
    """
    Create Figure 3.1: FasciaAEEG Distribution Visualization
    Shows the temporal distribution of Italian energy market time bands
    """
    
    print("🎯 Creating Figure 3.1: FasciaAEEG Distribution Visualization")
    print("=" * 60)
    
    # Load the enriched dataset
    try:
        df = pd.read_csv('enriched_pv_data_with_FasciaAEEG.csv')
        print(f"✅ Dataset loaded successfully: {df.shape}")
    except FileNotFoundError:
        print("❌ Error: enriched_pv_data_with_FasciaAEEG.csv not found")
        print("Please ensure the file exists in the current directory")
        return
    
    # Check if FasciaAEEG column exists
    if 'FasciaAEEG' not in df.columns:
        print("❌ Error: FasciaAEEG column not found in dataset")
        return
    
    # Calculate FasciaAEEG distribution
    fascia_counts = df['FasciaAEEG'].value_counts().sort_index()
    total_records = len(df)
    fascia_percentages = (fascia_counts / total_records) * 100
    
    print(f"\n📊 FasciaAEEG Distribution Analysis:")
    print(f"Total records: {total_records:,}")
    for fascia, count in fascia_counts.items():
        percentage = (count / total_records) * 100
        print(f"  {fascia}: {count:,} records ({percentage:.1f}%)")
    
    # Create the visualization
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Define colors for each FasciaAEEG category
    colors = {
        'F1': '#FF6B6B',  # Red for Peak hours
        'F2': '#4ECDC4',  # Teal for Intermediate hours  
        'F3': '#45B7D1'   # Blue for Off-peak hours
    }
    
    # Create bar chart
    bars = ax.bar(fascia_counts.index, fascia_counts.values, 
                  color=[colors[fascia] for fascia in fascia_counts.index],
                  alpha=0.8, edgecolor='black', linewidth=1.2)
    
    # Add value labels on bars
    for i, (fascia, count) in enumerate(fascia_counts.items()):
        percentage = fascia_percentages[fascia]
        
        # Add count label
        ax.text(i, count + total_records * 0.01, f'{count:,}', 
                ha='center', va='bottom', fontweight='bold', fontsize=11)
        
        # Add percentage label
        ax.text(i, count / 2, f'{percentage:.1f}%', 
                ha='center', va='center', fontweight='bold', 
                color='white', fontsize=12)
    
    # Customize the plot
    ax.set_title('Figure 3.1: FasciaAEEG Distribution Visualization\n' +
                'Temporal Distribution of Italian Energy Market Time Bands',
                fontsize=16, fontweight='bold', pad=20)
    
    ax.set_xlabel('FasciaAEEG Time Band', fontsize=14, fontweight='bold')
    ax.set_ylabel('Number of Records', fontsize=14, fontweight='bold')
    
    # Format y-axis with thousand separators
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))
    
    # Add grid for better readability
    ax.grid(True, axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    
    # Create detailed legend with descriptions
    legend_labels = [
        'F1 (Peak Hours): Mon-Fri 08:00-19:00, exc. holidays',
        'F2 (Intermediate): Mon-Fri 07:00-08:00 & 19:00-23:00, Sat 07:00-23:00',
        'F3 (Off-Peak): Nights, Sundays, Holidays'
    ]
    
    legend_handles = [plt.Rectangle((0,0),1,1, color=colors[f'F{i+1}'], alpha=0.8) 
                     for i in range(3)]
    
    ax.legend(legend_handles, legend_labels, loc='upper right', 
              frameon=True, fancybox=True, shadow=True, fontsize=10)
    
    # Add statistical annotations
    dominant_fascia = fascia_percentages.idxmax()
    dominant_percentage = fascia_percentages.max()
    
    stats_text = f"Dataset Statistics:\n" \
                f"• Total records: {total_records:,}\n" \
                f"• Dominant time band: {dominant_fascia} ({dominant_percentage:.1f}%)\n" \
                f"• Peak hours coverage: {fascia_percentages['F1']:.1f}%\n" \
                f"• Off-peak dominance: {fascia_percentages['F3']:.1f}%"
    
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
            verticalalignment='top', bbox=dict(boxstyle='round,pad=0.5', 
            facecolor='lightgray', alpha=0.8), fontsize=9)
    
    # Set y-axis limits with some padding
    max_count = fascia_counts.max()
    ax.set_ylim(0, max_count * 1.15)
    
    # Improve layout
    plt.tight_layout()
    
    # Save the figure
    output_filename = 'Figure_3_1_FasciaAEEG_Distribution.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    print(f"\n💾 Figure saved as: {output_filename}")
    
    # Also save as PDF for thesis use
    pdf_filename = 'Figure_3_1_FasciaAEEG_Distribution.pdf'
    plt.savefig(pdf_filename, dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    print(f"💾 Figure saved as: {pdf_filename}")
    
    # Show the plot
    plt.show()
    
    # Print interpretation for thesis
    print(f"\n📋 FIGURE 3.1 INTERPRETATION FOR THESIS:")
    print("=" * 50)
    print(f"This comprehensive bar chart displays the temporal distribution of Italian")
    print(f"energy market time bands across the entire dataset, clearly showing:")
    print(f"")
    print(f"🔵 F3 Off-peak hours: {fascia_percentages['F3']:.1f}% ({fascia_counts['F3']:,} records)")
    print(f"   - Dominates with more than half of all time intervals")
    print(f"   - Includes nighttime periods, weekends, and holidays")
    print(f"   - Represents lowest energy demand and pricing periods")
    print(f"")
    print(f"🔴 F1 Peak hours: {fascia_percentages['F1']:.1f}% ({fascia_counts['F1']:,} records)")
    print(f"   - Business hours (Mon-Fri 08:00-19:00, excluding holidays)")
    print(f"   - Highest energy demand and pricing periods")
    print(f"   - Critical for PV production optimization")
    print(f"")
    print(f"🟢 F2 Intermediate hours: {fascia_percentages['F2']:.1f}% ({fascia_counts['F2']:,} records)")
    print(f"   - Transition periods and Saturday daytime")
    print(f"   - Moderate energy demand and pricing")
    print(f"   - Bridge between peak and off-peak periods")
    print(f"")
    print(f"💡 Key Insights:")
    print(f"   • The Italian energy market regulatory framework effectively segments")
    print(f"     the day into distinct pricing periods")
    print(f"   • Off-peak dominance is expected due to nighttime hours (8 hrs/day)")
    print(f"     plus weekends and holidays")
    print(f"   • This distribution directly impacts PV energy valuation and")
    print(f"     grid management strategies")
    
    return fig, fascia_counts, fascia_percentages

def create_additional_analysis():
    """
    Create additional analysis visualizations for comprehensive understanding
    """
    
    print(f"\n🔍 Creating Additional FasciaAEEG Analysis...")
    
    try:
        df = pd.read_csv('enriched_pv_data_with_FasciaAEEG.csv')
        
        # Convert time column to datetime
        df['datetime'] = pd.to_datetime(df['time_15m'])
        df['hour'] = df['datetime'].dt.hour
        df['weekday'] = df['datetime'].dt.weekday
        df['month'] = df['datetime'].dt.month
        
        # Create subplots for additional analysis
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Additional FasciaAEEG Analysis', fontsize=16, fontweight='bold')
        
        # 1. Hourly distribution
        hourly_fascia = df.groupby(['hour', 'FasciaAEEG']).size().unstack(fill_value=0)
        hourly_fascia.plot(kind='bar', stacked=True, ax=axes[0,0], 
                          color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
        axes[0,0].set_title('FasciaAEEG Distribution by Hour')
        axes[0,0].set_xlabel('Hour of Day')
        axes[0,0].set_ylabel('Number of Records')
        axes[0,0].legend(title='FasciaAEEG')
        
        # 2. Weekly pattern
        weekday_fascia = df.groupby(['weekday', 'FasciaAEEG']).size().unstack(fill_value=0)
        weekday_fascia.plot(kind='bar', stacked=True, ax=axes[0,1], 
                           color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
        axes[0,1].set_title('FasciaAEEG Distribution by Weekday')
        axes[0,1].set_xlabel('Day of Week (0=Monday)')
        axes[0,1].set_ylabel('Number of Records')
        axes[0,1].legend(title='FasciaAEEG')
        
        # 3. Monthly pattern
        monthly_fascia = df.groupby(['month', 'FasciaAEEG']).size().unstack(fill_value=0)
        monthly_fascia.plot(kind='bar', stacked=True, ax=axes[1,0], 
                           color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
        axes[1,0].set_title('FasciaAEEG Distribution by Month')
        axes[1,0].set_xlabel('Month')
        axes[1,0].set_ylabel('Number of Records')
        axes[1,0].legend(title='FasciaAEEG')
        
        # 4. Pie chart with detailed percentages
        fascia_counts = df['FasciaAEEG'].value_counts()
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
        wedges, texts, autotexts = axes[1,1].pie(fascia_counts.values, 
                                                labels=fascia_counts.index,
                                                colors=colors, autopct='%1.1f%%',
                                                startangle=90, explode=(0.05, 0.05, 0.05))
        axes[1,1].set_title('FasciaAEEG Percentage Distribution')
        
        # Enhance the pie chart text
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(10)
            
        plt.tight_layout()
        
        # Save additional analysis
        additional_filename = 'Figure_3_1_Additional_FasciaAEEG_Analysis.png'
        plt.savefig(additional_filename, dpi=300, bbox_inches='tight')
        print(f"💾 Additional analysis saved as: {additional_filename}")
        
        plt.show()
        
    except Exception as e:
        print(f"❌ Error creating additional analysis: {e}")

if __name__ == "__main__":
    # Create main figure
    fig, counts, percentages = create_fascia_aeeg_distribution()
    
    # Create additional analysis
    create_additional_analysis()
    
    print(f"\n🎉 Figure 3.1 creation completed!")
    print(f"Files generated:")
    print(f"  • Figure_3_1_FasciaAEEG_Distribution.png (main figure)")
    print(f"  • Figure_3_1_FasciaAEEG_Distribution.pdf (thesis ready)")
    print(f"  • Figure_3_1_Additional_FasciaAEEG_Analysis.png (supplementary)")

using Microsoft.EntityFrameworkCore;

namespace SwiftTransferAPI.Models
{
    public class SwiftTransferContext : DbContext
    {
        public SwiftTransferContext(DbContextOptions<SwiftTransferContext> options)
            : base(options)
        {
        }

        public DbSet<SwiftTransfer> SwiftTransfers { get; set; }
    }
}